class posting_node:
    def __init__(self, **kwargs):
        self.posting = [kwargs['doc_id'], kwargs['term_freq'], kwargs['positions']]
        self.next = None


class postings_list:
    def __init__(self, **kwargs):
        self.term = kwargs['term']
        self.doc_frequency = 0
        self.head = None
        self.tail = None

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


class positional_index:
    def __init__(self, **kwargs):
        self.data_set = kwargs['data_set']
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

    def sort_index(self):
        temp = sorted(self.index.items())
        self.index = dict(temp)

    def get_postings_by_term(self, term):
        if term in self.index.keys():
            return self.index[term].posting

        else:
            return None

    def sample(self):
        import random
        terms = list(self.index.keys())
        rand_term = random.choice(terms)
        return self.index[rand_term].string()
