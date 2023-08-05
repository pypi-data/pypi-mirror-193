"""Named Entity Recognition module"""
import logging
from transformers import BertTokenizerFast, BertForTokenClassification, TokenClassificationPipeline
import torch
import pandas as pd
from ..config import paths

################# LOGGING #################
nerPipeLogger = logging.getLogger(__name__)
consoleHandler = logging.StreamHandler()
logFormatter = logging.Formatter(fmt=' %(name)s :: %(levelname)-4s :: %(message)s')

nerPipeLogger.setLevel(logging.DEBUG)
consoleHandler.setLevel(logging.DEBUG)

consoleHandler.setFormatter(logFormatter)
nerPipeLogger.addHandler(consoleHandler)

################# LOGGING #################

class NERModel:
    """Entity recognition along with the scores."""

    def __init__(self, model_name='marathi-ner',gpu_enabled:bool = False):
        self.model_name = model_name
        self.model_route = paths['tagger'][self.model_name]

        self.gpu_enabled = gpu_enabled
        self.device = 1 if (self.gpu_enabled and torch.cuda.is_available()) else -1

        self.pretrained_ner_model = BertForTokenClassification.from_pretrained(self.model_route)
        self.ner_tokenizer = BertTokenizerFast.from_pretrained(self.model_route)
        self.pipeline = TokenClassificationPipeline(
            task='marathi-ner',
            model=self.pretrained_ner_model,
            tokenizer=self.ner_tokenizer,
            framework="pt",
            aggregation_strategy='first',
            device=self.device,
        )

    def get_token_labels(self, text, details: str = "minimum",as_dict:bool = False):
        """Entity recognition of every token

        Args:
            text (str): An input text
            details (str, optional): (minimum, medium, all) - Defines the level of details
            to get from the prediction. Defaults to "minimum".
            as_dict (bool, optional): Used to define the print type. Defaults to False.

        Returns:
            list: lisr of entity tokens and scores
        """
        labels = pd.DataFrame(self.pipeline(text))

        labels['word'] = labels['word'].apply(lambda arr:list(arr.split(" ")))
        labels = labels.explode('word',ignore_index=True)
        columns = ['word','entity_group','score','start','end']

        if details == 'minimum':
            predicts = labels[columns[:2]]

        if details == "medium":
            predicts = labels[columns[:3]]

        if details == "all":
            predicts = labels[columns]

        if as_dict:
            return predicts.to_dict('records')
        return predicts

    def get_tokens(self,text):
        """Get only entity tokens

        Args:
            text (str): An input text

        Returns
            str: String of token entities
        """
        predictions = self.pipeline(text)

        token_labels  = ""
        for token in predictions:
            subwords = list(token['word'].strip().split(" "))
            for _ in subwords:
                token_labels  = token_labels + (" "  + token['entity_group'])

        token_labels = token_labels.lstrip()
        return token_labels


    def list_models(self):
        """Lists all models supported for named entity recognition."""
        print(" tagger models: ")
        for model in paths['tagger']:
            print("\t",model, ": ", paths['tagger'][model])
        for task in set(paths) - {'tagger'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])
