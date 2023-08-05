'''model_repo module is designed for ML practitioners and 
   comes with a flexibility to choose a model for desired tasks.'''
from .maha_fill import MaskFillModel
from .maha_gpt import GPTModel
from .maha_hate import HateModel
from .maha_ner import NERModel
from .maha_sentiment import SentimentModel
from .maha_similarity import SimilarityModel
