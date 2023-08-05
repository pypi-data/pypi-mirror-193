"""Text prediction module"""

from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import pandas as pd
from ..config import paths

class GPTModel:
    """Predicts next word or generates a complete sentence"""

    def __init__(self, model_name = 'marathi-gpt', gpu_enabled : bool = False):
        self.model_name = model_name
        self.model_route = paths['autocomplete'][self.model_name]
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_route)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_route)
        self.classifier = pipeline('text-generation',
                              model=self.model, tokenizer=self.tokenizer)
        pd.options.display.max_colwidth = None

    def next_word(self, text, num_of_predictions = 1):
        """Predicts the next word in the given sentence

        Args:
            text (str): An input text
            num_of_predictions (int, optional): number of predictions to be made. Defaults to 1.

        Returns:
            pandas DataFrame: Returns a pandas dataframe of predictions
        """
        result = self.classifier(text, max_new_tokens = 1,
                                 num_return_sequences = num_of_predictions)
        dataframe = pd.DataFrame.from_dict(result)
        return dataframe


    def complete_sentence(self, text, num_of_words = 25, num_of_predictions = 1):
        """Predicts the remanining blank words in the given sentence and completes a sentence.

        Args:
            text (str): An input text
            num_of_words (int, optional): number of words to be generated
            in the sentence. Defaults to 25.
            num_of_predictions (int, optional): number of predictions to be made. Defaults to 1.

        Returns:
           pandas DataFrame: Returns a pandas dataframe of predictions
        """
        result = self.classifier(text, max_new_tokens = num_of_words,
                                 num_return_sequences = num_of_predictions)
        dataframe = pd.DataFrame.from_dict(result)
        return dataframe

    def list_models(self):
        """Lists all models supported for text prediction."""
        print(" autocomplete models: ")
        for model in paths['autocomplete']:
            print("\t",model, ": ", paths['autocomplete'][model])
        for task in set(paths) - {'autocomplete'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])
                