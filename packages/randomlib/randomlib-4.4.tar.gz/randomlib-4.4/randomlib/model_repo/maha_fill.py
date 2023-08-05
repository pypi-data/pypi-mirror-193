"""Masked token prediction module"""
from transformers import AutoTokenizer, AutoModelForMaskedLM, BertTokenizer, BertForMaskedLM
from transformers import pipeline
import pandas as pd
from ..config import paths

class MaskFillModel:
    """Fills masked token."""

    def __init__(self, model_name='marathi-bert-v2', gpu_enabled:bool = False):
        self.model_name = model_name
        self.model_route = paths['mask_fill'][self.model_name]
        self.task = "fill-mask"

        if model_name == 'marathi-bert-v2':
            self.tokenizer = BertTokenizer.from_pretrained(self.model_route)
            self.model = BertForMaskedLM.from_pretrained(self.model_route)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_route)
            self.model = AutoModelForMaskedLM.from_pretrained(self.model_route)

        self.generator = pipeline(task = self.task,
                                    model=self.model,
                                    tokenizer=self.tokenizer)

    def predict_mask(self, text: str, details: str = "minimum", as_dict: bool = False):
        """Predicts a string for the masked token.

        Args:
            text (str): An input text
            details (str, optional): (minimum, medium, all) - Represents the detailedness
            of the result to be returned.
            as_dict (bool, optional): Used to define the print type. Defaults to False.

        Returns:
            pandas DataFrame: Returns a pandas dataframe
        """
        if text.find(self.tokenizer.mask_token) == -1:
            print("Please mask your sentence first!")
            return None
        predictions = pd.DataFrame(self.generator(text))
        predictions['token_str'] = predictions['token_str'].apply(lambda word: word.replace(" ",""))

        if details == 'minimum':
            custom_predict = predictions[['token_str','sequence']]

        if details == "medium":
            custom_predict = predictions[['token_str','score','sequence']]

        if details == "all":
            custom_predict = predictions

        if as_dict:
            return custom_predict.to_dict('records')
        return custom_predict

    def list_models(self):
        """Lists all models supported for masked token prediction."""
        print(" mask_fill models: ")
        for model in paths['mask_fill']:
            print("\t",model, ": ", paths['mask_fill'][model])
        for task in set(paths) - {'mask_fill'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])
