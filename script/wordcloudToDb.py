from pymongo import MongoClient
import json

total = []
with open("./data/政治/wordcloud.json", 'r') as fp:
    data = []
    temp = json.loads(fp.read())
    for key, value in temp.items():
        data.append({'name': key, 'value': value})
    total.append({
        "typeId": 0,
        "type": '政治',
        "content": {
            "data": data
        }
    })

with open("./data/文化/wordcloud.json", 'r') as fp:
    data = []
    temp = json.loads(fp.read())
    for key, value in temp.items():
        data.append({'name': key, 'value': value})
    total.append({
        "typeId": 1,
        "type": '文化',
        "content": {
            "data": data
        }
    })

with open("./data/社会/wordcloud.json", 'r') as fp:
    data = []
    temp = json.loads(fp.read())
    for key, value in temp.items():
        data.append({'name': key, 'value': value})
    total.append({
        "typeId": 2,
        "type": '社会',
        "content": {
            "data": data
        }
    })

conn = MongoClient('127.0.0.1', 27017)
db = conn.analyse
wordcloud = db.wordcloud
x = wordcloud.insert_many(total)
print(x)
