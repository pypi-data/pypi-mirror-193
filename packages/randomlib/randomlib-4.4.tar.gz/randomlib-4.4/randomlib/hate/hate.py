"""Inherits methods from HateModel class of model_repo"""
from randomlib.model_repo.maha_hate import HateModel

class HateAnalyzer(HateModel):
    """Module uses 'mahahate-bert' model for hate score analysis."""

    def __init__(self):
        self.model_name = 'mahahate-bert'
        super().__init__(self.model_name)
