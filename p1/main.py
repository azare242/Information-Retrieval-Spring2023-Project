from __future__ import unicode_literals

from p1.model.data_set import data_set
from p1.util.pre_processor import pre_processor
from hazm import *

if __name__ == '__main__':
    data = data_set()
    _doc = data.docs[0]
    n = Normalizer().normalize(_doc.content)
    print(f'Content:\n{_doc.content}')
    print(f'Normalized:\n{n}')
    t = WordTokenizer().tokenize(n)
    print(f'Tokenized:\n{t}')
    li = stopwords_list()
    special_chars = ['!', '\"', '#', '(', ')', '*', '-', '.', '/', ':', '[', ']', '«', '»', '،', '؛', '؟']
    for x in special_chars:
        li.append(x)
    s = []
    st = Stemmer()
    for x in t:
        tem = st.stem(x)
        if x not in li:
            s.append(x)
    lem = []
    lm = Lemmatizer()
    for x in t:
        lem.append(
            lm.lemmatize(x)
        )
    print(f'Stems without stopwords:\n{s}')
    print(f'Lemmatizeds:\n{lem}')


#file = open('../IR_data_news_12k.json')