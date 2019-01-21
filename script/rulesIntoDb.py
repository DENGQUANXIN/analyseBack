import pandas as pd
from pymongo import MongoClient

df = pd.read_csv("./data/rules/all.txt")
dfgpByWord1 = df.groupby("word1")
dfgpByWord2 = df.groupby("word2")

dfgpIndexs1 = []
for item in dfgpByWord1.groups:
    dfgpIndexs1.append(item)

dfgpIndexs2 = []
for item in dfgpByWord2.groups:
    dfgpIndexs2.append(item)

dfgpIndexs = list(set(dfgpIndexs1 + dfgpIndexs2))
result = []
for index in dfgpIndexs:
    connectWords = []
    count = 0
    temp = {}
    if(index in dfgpByWord1.groups):
        for item in dfgpByWord1.groups[index]:
            if(df.ix[item]['word2'] not in temp.keys()):
                connectWords.append({"name": df.ix[item]['word2'], "value": int(df.ix[item]['count'])})
                temp[df.ix[item]['word2']] = count
                count += 1
            else:
                connectWords[temp[df.ix[item]['word2']]]['value'] += int(df.ix[item]['count'])
    if(index in dfgpByWord2.groups):
        for item in dfgpByWord2.groups[index]:
            if(df.ix[item]['word1'] not in temp.keys()):
                connectWords.append({"name": df.ix[item]['word1'], "value": int(df.ix[item]['count'])})
                temp[df.ix[item]['word1']] = count
                count += 1
            else:
                connectWords[temp[df.ix[item]['word1']]]['value'] += int(df.ix[item]['count'])
    result.append({'centerword': index, 'connectwords': connectWords})

print(result[0])

conn = MongoClient('127.0.0.1', 27017)
db = conn.analyse
connect = db.connect
x = connect.insert_many(result)
print(x)
