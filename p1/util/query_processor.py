from hazm import *


class query_processor:
    def __init__(self):
        self.normalizer = Normalizer()
        self.tokenizer = WordTokenizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()
        self.stopwords = self.create_stopwords_list()

    def create_stopwords_list(self):
        li = stopwords_list()
        special_chars = ['!', '\"', '#', '(', ')', '*', '-', '.', '/', ':', '[', ']', '«', '»', '،', '؛', '؟']
        for x in special_chars:
            li.append(x)
        return li

    def proceess(self, query):
        norm = self.normalizer.normalize(query)
        tokens = self.tokenizer.tokenize(norm)
        stems = []
        for token in tokens:
            temp_stem = self.stemmer.stem(token)
            if temp_stem not in self.stopwords:
                stems.append(temp_stem)
        lemms = []
        for stem in stems:
            lemms.append(self.lemmatizer.lemmatize(stem))
        return lemms
