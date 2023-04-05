import json
from model.doc import doc


def load():
    docs = []
    with open("../IR_data_news_12k.json", encoding='utf-8') as file:
        read = json.load(file)
        i = 1
        for data in read:
            docs.append(
                doc(id=i,
                    title=read[data]['title'],
                    content=read[data]['content'],
                    url=read[data]['url'])
            )
            i += 1
    return docs
