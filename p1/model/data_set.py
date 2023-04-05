from model.doc import doc
import json
from util import data_loader
from p1.util.pre_processor import pre_processor


class data_set:
    def __init__(self):
        self.docs = data_loader.load()
        self.pre_processor = pre_processor()

        self.processed_tokens = self.pre_process_data()

    def pre_process_data(self):
        return self.normalize()

    def normalize(self):
        norms = {}
        for doc in self.docs:
            norms[doc.id] = self.pre_processor.normalizer.normalize(doc.content)

        return self.tokenize(norms)

    def tokenize(self, norms):
        tokens = {}
        for doc_id, content in zip(norms.keys(), norms.values()):
            tokens[doc_id] = self.pre_processor.tokenizer.tokenize(content)

        return self.stem(tokens)

    def stem(self, tokens):
        stems = {}
        for doc_id, token_list in zip(tokens.keys(), tokens.values()):
            stem_temp = []
            for x in token_list:
                stem_temp.append(
                    self.pre_processor.stemmer.stem(x)
                )
            stems[doc_id] = stem_temp

        return self.lemmatize(stems)

    def lemmatize(self, stems):
        lemmatizes = {}
        for doc_id, stem_list in zip(stems.keys(), stems.values()):
            lemmatize_temp = []
            for x in stem_list:
                temp_lemmatized = self.pre_processor.lemmatizer.lemmatize(x)
                if not self.pre_processor.is_stopword(temp_lemmatized):
                    lemmatize_temp.append(
                        self.pre_processor.lemmatizer.lemmatize(x)
                    )
            lemmatizes[doc_id] = lemmatize_temp
        return lemmatizes


    def print_data_set(self):
        for doc in self.docs:
            print(f'{doc.title} : {doc.url}')

    def print_by_doc_id(self, idx):
        if idx - 1 > len(self.docs) or idx - 1 < 0:
            return
        print(f'{self.docs[idx - 1].title} : {self.docs[idx - 1].url}')
