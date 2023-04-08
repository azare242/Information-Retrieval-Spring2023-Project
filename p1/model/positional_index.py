class postings_list:
    def __init__(self, **kwargs):
        self.term = kwargs['term']
        self.postings = []

    def doc_frequency(self):
        return len(self.postings)

    def term_frequency(self, doc_id):
        for p in self.postings:
            if p[0] == doc_id:
                return p[1]
        return -1

    def positions(self, doc_id):
        for p in self.postings:
            if p[0] == doc_id:
                return p[2]
        return None

    def add(self, doc_id, term_frequency, positions):
        self.postings.append([doc_id, term_frequency, positions])


class positional_index:
    def __init__(self, **kwargs):
        self.data_set = kwargs['data_set']
        self.index = {}

    def construction(self):
        for doc_id, tokens in zip(self.data_set.processed_tokens.keys(), self.data_set.processed_tokens.values()):
            for pos, term in enumerate(tokens):
                if term not in self.index.keys():
                    self.index[term] = postings_list(term=term)
                _postings_list = self.index[term]
                if len(_postings_list.postings) != 0 and _postings_list.postings[-1][0] == doc_id:
                    _postings_list.postings[-1][1] += 1
                    _postings_list.postings[-1][2].append(pos)
                else:
                    _postings_list.add(doc_id, 1, [pos])

    def get_postings_by_term(self, term):
        if term in self.index.keys():
            return self.index[term].postings

        else:
            return None
