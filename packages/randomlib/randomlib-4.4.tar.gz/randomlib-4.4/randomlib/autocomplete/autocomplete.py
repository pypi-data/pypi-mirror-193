"""Inherits methods from GPTModel class of model_repo"""
from randomlib.model_repo.maha_gpt import GPTModel

class TextGenerator(GPTModel):
    """Module uses 'marathi-gpt' model for text generation."""

    def __init__(self):
        self.model_name = 'marathi-gpt'
        super().__init__(self.model_name)
