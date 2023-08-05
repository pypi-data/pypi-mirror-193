"""Sentence Similarity Analyzer module"""
from sentence_transformers import SentenceTransformer, util
from ..config import paths

class SimilarityModel:
    """Provides sentence embeddings and sentence similarity score functionalities."""

    def __init__(self, model_name = 'marathi-sentence-similarity-sbert', gpu_enabled:bool = False):
        self.model_name = model_name
        self.model_route = paths['similarity'][self.model_name]
        self.model = SentenceTransformer(self.model_route)

    def embed_sentences(self,sentences):
        """Embeds the input sentence

        Args:
            sentences (str): An input text

        Returns:
            list: array of embeddings
        """
        sentence_embeddings = self.model.encode(sentences)
        return sentence_embeddings

    def get_similarity_score(self, source_sentence, sentences, as_dict: bool = False):
        """Checks the similarity of a sentence with respect to array of sentences

        Args:
            source_sentence (str): An input text
            sentences (list): List of input sentences to be compared with the source sentence
            as_dict (bool, optional): Used to define the print type. Defaults to False.

        Returns:
            list: returns a list of similarity scores.
        """
        embeddings1 = self.embed_sentences(source_sentence)
        embeddings2 = self.embed_sentences(sentences)
        cosine_scores = util.cos_sim(embeddings1, embeddings2)
        result_np_array = cosine_scores.numpy()[0]

        if as_dict:
            dictionary = {}
            if isinstance(sentences, str):
                sentences = [sentences]
            for i, sentence in enumerate(sentences):
                dictionary[sentence] =  result_np_array[i]
            return dictionary
        return result_np_array

    def list_models(self):
        """Lists all sentence similarity models."""
        print(" similarity models: ")
        for model in paths['similarity']:
            print("\t",model, ": ", paths['similarity'][model])
        for task in set(paths) - {'similarity'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])
