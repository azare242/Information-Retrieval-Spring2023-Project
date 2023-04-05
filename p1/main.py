from __future__ import unicode_literals

from p1.model.data_set import data_set
from p1.util.pre_processor import pre_processor
from hazm import *

if __name__ == '__main__':
    data = data_set()
    data.print_by_doc_id(5)
    print(data.processed_tokens[5])


#file = open('../IR_data_news_12k.json')