"""Inherits methods from MaskFillModel class of model_repo"""
from randomlib.model_repo.maha_fill import MaskFillModel

class MaskPredictor(MaskFillModel):
    """Module uses 'marathi-bert-v2' model for masked token prediction."""

    def __init__(self):
        self.model_name = 'marathi-bert-v2'
        super().__init__(self.model_name)
