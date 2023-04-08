
class postings_list:
    def __init__(self, **kwargs):
        self.term = kwargs['term']
        self.positional_list = {}

    def insert(self, doc_id, position):
        if doc_id not in self.positional_list.keys():
            self.positional_list[doc_id] = []

        self.positional_list[doc_id].append(position)


class positional_index:
    def __init__(self):
        self.postings_lists = []

    # TO DO: construction
    """
    def construction(self, data_set):
        pass
    """
