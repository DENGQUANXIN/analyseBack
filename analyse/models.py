from mongoengine import Document
import mongoengine


class wordcloud(Document):
    typeId = mongoengine.IntField()
    type = mongoengine.StringField(max_length=50)
    content = mongoengine.ListField()


class chart(Document):
    typeId = mongoengine.IntField()
    type = mongoengine.StringField(max_length=50)
    content = mongoengine.DictField()


class zhihu(Document):
    typeId = mongoengine.IntField()
    subtype = mongoengine.StringField()
    type = mongoengine.StringField(max_length=50)
    content = mongoengine.DictField()


class connect(Document):
    centerword = mongoengine.StringField()
    connectwords = mongoengine.ListField()
