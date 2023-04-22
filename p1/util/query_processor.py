from __future__ import unicode_literals
from hazm import *
from p1.model.positional_index import *






class query_processor:
    def __init__(self, **kwargs):
        self.normalizer = Normalizer()
        self.tokenizer = WordTokenizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()
        self.stopwords = self.create_stopwords_list()
        self.pindex = kwargs['pindex']

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


        for x in res:
            for y in x[0]:
                if not y in self.pindex.index.keys():
                    x[0].remove(y)
            if len(x[0]) == 0:
                res.remove(x)
        return res


    def AND(self, p1, p2):

        res = []
        i = j = 0
        while i < len(p1) and j < len(p2):
            if p1[i] == p2[j]:
                res.append(p1[i])
                i += 1
                j += 1
            elif p1[i] < p2[j]:
                i += 1
            else:
                j += 1
        return res

    def AND_NOT(self, p, p_not):
        res = []
        i = j = 0
        while i < len(p) and j < len(p_not):
            if p[i] == p_not[j]:
                i += 1
                j += 1
            elif p[i] < p_not[j]:
                res.append(p[i])
                i += 1
            else:
                j += 1
        while i < len(p):
            res.append(p[i])
            i += 1
        return res

    def phrase(self, pp_phrase):
        doc_ids_poss = []
        for x in pp_phrase:
            doc_ids_poss.append(self.pindex.index[x].get_docid_positions_as_dict())
        doc_ids = [sorted(list(y.keys())) for y in doc_ids_poss]
        current = doc_ids[0]
        for i in range(1, len(doc_ids)):
            current = self.AND(current, doc_ids[i])
        return current

    def operate(self, _curr, _next, mode):
        if mode == 'none':
            return self.AND(_curr, _next)
        elif 'not' in mode:
            return self.AND_NOT(_curr, _next)

    def find_terms(self, pp_text):
        res = []
        for x in pp_text:
            if 'phrase' in x[1]:
                y = self.phrase(x[0])
                res.append((y, 'not' if 'not' in x[1] else 'none'))
            else:
                res.append((self.pindex.index[x[0][0]].get_docid_as_list(), x[1]))
        return res


    def answer(self, query):
        pp_text = self.process_text(query)
        terms = self.find_terms(pp_text)
        current = terms[0][0]
        for i in range(1, len(terms)):
            current = self.operate(current, terms[i][0], terms[i][1])
        return current