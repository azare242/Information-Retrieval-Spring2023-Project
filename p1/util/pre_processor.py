from hazm import *


class pre_processor:
    def __init__(self):
        self.tokenizer = WordTokenizer()
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()
