"""Inherits methods from SimilarityModel class of model_repo"""
from randomlib.model_repo.maha_similarity import SimilarityModel

class SimilarityAnalyzer(SimilarityModel):
    """Module uses 'marathi-sentence-similarity-sbert' model for text generation."""

    def __init__(self):
        self.model_name =  'marathi-sentence-similarity-sbert'
        super().__init__(self.model_name)
