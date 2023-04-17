from __future__ import unicode_literals
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
        special_chars = ['#', '(', ')', '*', '-', '.', '/', ':', '[', ']', '،', '؛', '؟']
        for x in special_chars:
            li.append(x)
        return li

    def process_text(self, query):
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
        n = len(lemms)
        res = []
        parentheses_flag = False
        not_flag = 0
        new = []
        for i in range(n):
            if lemms[i] == '!':
                not_flag = 1
            elif lemms[i] == '«':
                parentheses_flag = True
            elif lemms[i] == '»':
                state = 'phrase' if not_flag != 2 else 'not-phrase'
                parentheses_flag, not_flag = False, 0
                res.append((new, state))
                new = []
            else:
                if not_flag == 1 and parentheses_flag:
                    new.append(lemms[i])
                    not_flag = 2
                elif parentheses_flag:
                    new.append(lemms[i])
                elif not_flag == 1:
                    res.append(([lemms[i]], 'not'))
                    not_flag = 0
                else:
                    res.append(([lemms[i]], 'none'))

        return res
