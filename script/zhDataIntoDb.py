from pymongo import MongoClient
import json

# 词云数据整理
with open('./wordcloud.json', 'r') as fp:
    temp = json.loads(fp.read())
    wordcloud = []
    for key, value in temp.items():
        wordcloud.append({"name": key, "value": value})

# 行业数据整理
with open('./政治/business.json', 'r') as fp:
    business1 = json.loads(fp.read())
with open('./文化/business.json', 'r') as fp:
    business2 = json.loads(fp.read())
with open('./社会/business.json', 'r') as fp:
    business3 = json.loads(fp.read())

keyList = list(set(business1.keys()) | set(business2.keys()) | set(business3.keys()))
buslabels = keyList
busPolitics = []
busCulture = []
busSocial = []
for key in keyList:
    value = business1[key] if(key in business1.keys()) else 0
    busPolitics.append(value)
    value = business2[key] if(key in business2.keys()) else 0
    busCulture.append(value)
    value = business3[key] if(key in business3.keys()) else 0
    busSocial.append(value)

# 专业数据整理
with open('./政治/major.json', 'r') as fp:
    major1 = json.loads(fp.read())
with open('./文化/major.json', 'r') as fp:
    major2 = json.loads(fp.read())
with open('./社会/major.json', 'r') as fp:
    major3 = json.loads(fp.read())

keyList = list(set(major1.keys()) | set(major2.keys()) | set(major3.keys()))
majlabels = keyList
majPolitics = []
majCulture = []
majSocial = []
for key in keyList:
    value = major1[key] if(key in major1.keys()) else 0
    majPolitics.append(value)
    value = major2[key] if(key in major2.keys()) else 0
    majCulture.append(value)
    value = major3[key] if(key in major3.keys()) else 0
    majSocial.append(value)

# 位置数据整理
with open('./city_coordinates.json', 'r') as fp:
    coordinates = json.loads(fp.read())

locPolitics = []
locCulture = []
locSocial = []
with open('./政治/location.json', 'r') as fp:
    loc1 = json.loads(fp.read())
    for key, value in loc1.items():
        if key in coordinates.keys():
            locPolitics.append({'name': key, 'value': coordinates[key]+[value]})

with open('./文化/location.json', 'r') as fp:
    loc2 = json.loads(fp.read())
    for key, value in loc2.items():
        if key in coordinates.keys():
            locCulture.append({'name': key, 'value': coordinates[key]+[value]})
with open('./社会/location.json', 'r') as fp:
    loc3 = json.loads(fp.read())
    for key, value in loc3.items():
        if key in coordinates.keys():
            locSocial.append({'name': key, 'value': coordinates[key]+[value]})


conn = MongoClient('127.0.0.1', 27017)
db = conn.analyse
chart = db.zhihu

total = [
    {
        'typeId': 0,
        'type': '文章分析',
        'subtype': '文章类别',
        'content': {
            'data': [{
                'name': '政治',
                'value': 30
            }, {
                'name': '文化',
                'value': 151
            }, {
                'name': '社会',
                'value': 268
            }, {
                'name': '其它',
                'value': 51
            }]
        }
    },
    {
        'typeId': 1,
        'type': '文章分析',
        'subtype': '文章词云',
        'content': {
            'data': wordcloud
        }
    },
    {
        'typeId': 2,
        'type': '文章分析',
        'subtype': '作者性别分布',
        'content': {
            'data': [{
                'name': '男',
                'value': 362
            }, {
                'name': '女',
                'value': 97
            }, {
                'name': '未填写',
                'value': 41
            }]
        }
    },
    {
        'typeId': 3,
        'type': '文章分析',
        'subtype': '点赞评论数',
        'content': {
            'label': [
                '评论数<10\n\n\n\n\n点赞数<100',
                '评论数10-50\n\n\n\n\n点赞数100-500',
                '评论数50-100\n\n\n\n\n点赞数500-1000',
                '评论数>100\n\n\n\n\n点赞数>1000'
            ],
            'comments': [445, 44, 10, 1],
            'likes': [471, 22, 6, 1]
        }
    },
    {
        'typeId': 4,
        'type': '评论分析',
        'subtype': '评论者性别分布',
        'content': {
            'political': [{
                'value': 1147,
                'name': '男'
            },
                {
                'value': 767,
                'name': '女'
            },
                {
                'value': 708,
                'name': '未填写'
            }
            ],
            'culture': [{
                'value': 227,
                'name': '男'
            },
                {
                'value': 131,
                'name': '女'
            },
                {
                'value': 142,
                'name': '未填写'
            }
            ],
            'social': [{
                'value': 498,
                'name': '男'
            },
                {
                'value': 330,
                'name': '女'
            },
                {
                'value': 726,
                'name': '未填写'
            }
            ]
        }
    },
    {
        'typeId': 5,
        'type': '评论分析',
        'subtype': '评论者位置分布',
        'content': {
            'politics': locPolitics,
            'culture': locCulture,
            'social': locSocial
        }
    },
    {
        'typeId': 6,
        'type': '评论分析',
        'subtype': '评论者行业分布',
        'content': {
            'labels': buslabels,
            'politics': busPolitics,
            'culture': busCulture,
            'social': busSocial
        }
    },
    {
        'typeId': 7,
        'type': '评论分析',
        'subtype': '评论者专业分布',
        'content': {
            'labels': majlabels,
            'politics': majPolitics,
            'culture': majCulture,
            'social': majSocial
        }
    }
]

x = chart.insert_many(total)
print(x)
