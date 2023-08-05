"""Inherits methods from NERModel class of model_repo"""
from randomlib.model_repo.maha_ner import NERModel

class EntityRecognizer(NERModel):
    """Module uses 'marathi-ner' model for entity recognition."""

    def __init__(self):
        self.model_name = 'marathi-ner'
        super().__init__(self.model_name)
