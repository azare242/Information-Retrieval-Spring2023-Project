class posting_node:
    def __init__(self, **kwargs):
        self.posting = [kwargs['doc_id'], kwargs['term_freq'], kwargs['positions'], 0]
        self.next = None


class postings_list:
    def __init__(self, **kwargs):
        self.term = kwargs['term']
        self.doc_frequency = 0
        self.head = None
        self.tail = None
        self.champion = None

    def get_tfidf_by_docid(self, docid):
        p = self.head
        while p is not None:
            if p.posting[0] == docid:
                return p.posting[-1]
            p = p.next
        return 0

    def string(self):
        p = self.head
        s = f'{self.term}: \n ['
        while p.next is not None:
            x = p.posting
            s += f'<<doc_id : {x[0]}, term_frequency : {x[1]}, positions : {x[2]}>> --> '
            p = p.next
        s += f'<<doc_id : {p.posting[0]}, frequency : {p.posting[1]}, positions : {p.posting[2]}>>]\n doc_frequency : {self.doc_frequency} '
        return s

    def add(self, doc_id, term_frequency, positions):
        new_node = posting_node(doc_id=doc_id, term_freq=term_frequency, positions=positions)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.doc_frequency += 1

    def get_docid_as_list(self):
        res = []
        p = self.head
        while p is not None:
            res.append(p.posting[0])
            p = p.next
        return res

    def get_docid_tfidf_as_list(self):
        res = []
        p = self.head
        while p is not None:
            res.append([p.posting[0], [p.posting[-1]]])
            p = p.next
        return res

    def get_docid_positions_as_dict(self):
        res = {}
        p = self.head
        while p is not None:
            res[p.posting[0]] = p.posting[2]
            p = p.next
        return res

    def construct_champion_list(self):
        p = self.head
        tmp_ = []
        while p is not None:
            tmp_.append((p.posting[0], p.posting[-1]))
            p = p.next
        __doc_ids = [__x[0] for __x in sorted(tmp_, key=lambda __x: __x[1])]
        if len(__doc_ids) < 10:
            self.champion = __doc_ids[::-1]
        else:
            self.champion = __doc_ids[::-1][:10]


class positional_index:
    def __init__(self, **kwargs):
        self.data_set = kwargs['data_set']
        self.N = self.data_set.N()
        self.index = {}
        self.construction()

    def construction(self):
        for doc_id, tokens in zip(self.data_set.processed_tokens.keys(), self.data_set.processed_tokens.values()):
            for pos, term in enumerate(tokens):
                if term not in self.index.keys():
                    self.index[term] = postings_list(term=term)
                _postings_list = self.index[term]
                if _postings_list.head is not None and _postings_list.tail.posting[0] == doc_id:
                    _postings_list.tail.posting[1] += 1
                    _postings_list.tail.posting[2].append(pos)
                else:
                    _postings_list.add(doc_id, 1, [pos])
        self.sort_index()
        self.compute_tfidf()

    def compute_tfidf(self):
        from math import log10
        for term, poslist in zip(self.index.keys(), self.index.values()):
            idf = log10(self.N / poslist.doc_frequency)
            t = poslist.head
            while t is not None:
                tf = 1 + log10(t.posting[1])
                t.posting[3] = tf * idf
                t = t.next
            poslist.construct_champion_list()

    def sort_index(self):
        temp = sorted(self.index.items())
        self.index = dict(temp)

    def get_postings_by_term(self, term):
        if term in self.index.keys():
            return self.index[term].posting

        else:
            return None

    def get_doc_vector_length(self, doc_id):
        res = 0
        for term in self.index.keys():
            tfidf = self.index[term].get_tfidf_by_docid(doc_id)
            res += tfidf ** 2
        return res ** 0.5

    def sample(self):
        import random
        terms = list(self.index.keys())
        rand_term = random.choice(terms)
        return self.index[rand_term].string()
