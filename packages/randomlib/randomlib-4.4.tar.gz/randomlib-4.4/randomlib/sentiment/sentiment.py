"""Inherits methods from SentimentModel class of model_repo"""
from randomlib.model_repo.maha_sentiment import SentimentModel

class SentimentAnalyzer(SentimentModel):
    """Module uses 'MarathiSentiment' model for sentiment score analysis."""

    def __init__(self):
        self.model_name = 'MarathiSentiment'
        super().__init__(self.model_name)
