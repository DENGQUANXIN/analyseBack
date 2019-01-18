from django.test import TestCase
from .models import wordcloud, chart, zhihu, connect
import mongoengine


# Create your tests here.
class wordcloudTestCase(TestCase):
    def test_wordcloud_typeId_type(self):
        obj = wordcloud.objects.filter(typeId=0)[0]
        self.assertIs(type(obj.typeId), int)

    def test_wordcloud_type_type(self):
        obj = wordcloud.objects.filter(typeId=0)[0]
        self.assertIs(type(obj.type), str)

    def test_wordcloud_content_type(self):
        obj = wordcloud.objects.filter(typeId=0)[0]
        self.assertIs(type(obj.content), mongoengine.base.datastructures.BaseList)


class chartTestCase(TestCase):
    def test_chart_typeId_type(self):
        for typeId in range(0, 5):
            obj = chart.objects.filter(typeId=typeId)[0]
            self.assertIs(type(obj.typeId), int)

    def test_chart_type_type(self):
        for typeId in range(0, 5):
            obj = chart.objects.filter(typeId=typeId)[0]
            self.assertIs(type(obj.type), str)

    def test_chart_content_type(self):
        for typeId in range(0, 5):
            obj = chart.objects.filter(typeId=typeId)[0]
            self.assertIs(type(obj.content), mongoengine.base.datastructures.BaseDict)


class zhihuTestCase(TestCase):
    def test_zhihu_typeId_type(self):
        for typeId in range(0, 8):
            obj = zhihu.objects.filter(typeId=typeId)[0]
            self.assertIs(type(obj.typeId), int)

    def test_zhihu_type_type(self):
        for typeId in range(0, 8):
            obj = zhihu.objects.filter(typeId=typeId)[0]
            self.assertIs(type(obj.type), str)

    def test_zhihu_subtype_type(self):
        for typeId in range(0, 8):
            obj = zhihu.objects.filter(typeId=typeId)[0]
            self.assertIs(type(obj.type), str)

    def test_zhihu_content_type(self):
        for typeId in range(0, 8):
            obj = zhihu.objects.filter(typeId=typeId)[0]
            self.assertIs(type(obj.content), mongoengine.base.datastructures.BaseDict)


class connectTestCase(TestCase):
    def test_connect_centerword_type(self):
        obj = connect.objects.filter(centerword='西藏')[0]
        self.assertIs(type(obj.centerword), str)

    def test_connect_connectwords_type(self):
        obj = connect.objects.filter(centerword='西藏')[0]
        self.assertIs(type(obj.connectwords), mongoengine.base.datastructures.BaseList)
