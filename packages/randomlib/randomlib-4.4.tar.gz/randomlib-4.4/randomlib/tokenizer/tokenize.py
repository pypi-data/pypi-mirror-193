"""Tokenize module"""

class Tokenize:
    """Provides sentence and word tokenization functionalties."""

    def __init__(self,lang='mr'):
        self.lang = lang

    def sentence_tokenize_mr(self, txt):
        """Internal function for Marathi sentence tokenization, not meant for programmer's usage

        Args:
            txt (str): An input text consisting of multiple sentences.

        Returns:
            list: list of sentences.
        """
        punc_for_sentence_end = '''.!?'''
        sentences = []
        string = ""
        for i in txt:
            if i == "\n":
                continue
            if i not in punc_for_sentence_end:
                string += i
            else:
                string += i
                sentences.append(string)
                string = ""

        return sentences

    def sentence_tokenize(self, txt):
        """Tokenizes sentences from paragraph or set of sentences.

        Args:
            txt (str): An input text consisting of multiple sentences.

        Returns:
            list: list of sentences.
        """
        if self.lang == 'mr':
            return self.sentence_tokenize_mr(txt)


    def word_tokenize_mr(self, txt, punctuation):
        """Internal function for Marathi word tokenization, not meant for programmer's usage

        Args:
            txt (str): An input text.
            punctuation (bool): Decides whether to tokenize punctuation marks

        Returns:
            list: list of words.
        """
        punc = '''\\!()-[]{};:'",<>./?@#$%^&*_~'''
        if punctuation:
            string = ""
            tokens = []
            for ele in txt:
                if ele in punc:
                    if string:
                        tokens.append(string)
                        string = ""
                    tokens.append(ele)
                elif ele == " ":
                    if string:
                        tokens.append(string)
                        string = ""
                else:
                    string += ele
            if string:
                tokens.append(string)
                string = ""
            return tokens

        for ele in txt:
            if ele in punc:
                txt = txt.replace(ele, " ")
        result = txt.split()
        return result

    def word_tokenize(self, line, punctuation=True):
        """Tokenizes words from sentences.

        Args:
            line (str): An input text.
            punctuation (bool, optional): Decides whether to tokenize punctuation marks. 
            Defaults to True.

        Returns:
            list: list of words
        """
        if self.lang == 'mr':
            result = self.word_tokenize_mr(line, punctuation)
            return result
