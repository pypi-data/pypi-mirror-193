"""Sentiment Analysis Module"""
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import pandas as pd
from ..config import paths

class SentimentModel:
    """Labels text as positive / negative / neutral and provides score for the same."""

    def __init__(self, model_name='MarathiSentiment', gpu_enabled:bool = False):
        self.model_name = model_name
        self.model_route = paths['sentiment'][self.model_name]
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_route)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_route)
        self.classifier = pipeline('text-classification',
                              model=self.model, tokenizer=self.tokenizer)
    def get_polarity_score(self, text):
        """Gives the sentiment score of a sentence.

        Args:
            text (str): An input string

        Returns:
            pandas DataFrame: Returns a pandas dataframe of label and score
        """
        result = self.classifier(text)
        dataframe = pd.DataFrame.from_dict(result)
        return dataframe

    def list_supported_labels(self):
        """Lists the labels returned by classification"""
        print('Supported labels: \n -Positive\n -Negative\n -Neutral\n')

    def list_models(self):
        """Lists all models supported for sentiment analysis."""

        print(" sentiment models: ")
        for model in paths['sentiment']:
            print("\t",model, ": ", paths['sentiment'][model])
        for task in set(paths) - {'sentiment'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])
                