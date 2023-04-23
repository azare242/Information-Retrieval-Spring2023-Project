from p1.model.data_set import data_set
from model.positional_index import positional_index
from util.query_processor import query_processor
def print_query_result(list_doc_ids: list, DataSet: data_set):
    for doc_id in list_doc_ids[:5]:
        DataSet.print_by_doc_id(doc_id)
if __name__ == '__main__':
    data = data_set()
    PositionalIndex = positional_index(data_set=data)
    QueryProcessor = query_processor(pindex=PositionalIndex)
    Q1 = QueryProcessor.answer('باشگاه های فوتسال آسیا')
    Q2 = QueryProcessor.answer('باشگاه های فوتسال ! آسیا')
    Q3 = QueryProcessor.answer('"سهمیه المپیک"')
    Q4 = QueryProcessor.answer('طلای "لیگ برتر" ! والیبال')
    Q5 = QueryProcessor.answer('مایکل ! جردن')
    l = [Q1, Q2, Q3, Q4, Q4]
    for i in l:
        print_query_result(i, data)
        print('---------------------------------------------')


