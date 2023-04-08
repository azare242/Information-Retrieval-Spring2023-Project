#from __future__ import unicode_literals

from p1.model.data_set import data_set
from model.positional_index import positional_index
#from hazm import *

if __name__ == '__main__':
    import random
    data = data_set()
    t1 = random.choice(data.processed_tokens)
    t2 = random.choice(t1)
    PositionalIndex = positional_index(data_set=data)

    print(PositionalIndex.get_postings_by_term(t2))