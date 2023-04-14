from p1.model.data_set import data_set
from model.positional_index import positional_index
from util.query_processor import query_processor

if __name__ == '__main__':
    print('please wait, data is processing...')
    data = data_set()
    PositionalIndex = positional_index(data_set=data)
    print('processing ends')
    while True:
        term = input('>> ')
        if term == 'exit':
            break
        if term in PositionalIndex.index.keys():
            print(PositionalIndex.index[term].string())
        else:
            print('term not found')
