from hazm import *


class pre_processor:
    def __init__(self):
        self.tokenizer = WordTokenizer()
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()
        self.stop_words = stopwords_list()

    def is_stopword(self, word):
        return word in self.stop_words