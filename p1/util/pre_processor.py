from hazm import *


class pre_processor:
    def __init__(self):
        self.tokenizer = WordTokenizer()
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()
        self.stop_words = self.create_stopwords_list()

    def create_stopwords_list(self):
        li = stopwords_list()
        special_chars = ['!', '\"', '#', '(', ')', '*', '-', '.', '/', ':', '[', ']', '«', '»', '،', '؛', '؟']
        for x in special_chars:
            li.append(x)
        return li

    def is_stopword(self, word):
        return word in self.stop_words
