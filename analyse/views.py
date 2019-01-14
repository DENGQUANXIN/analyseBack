from django.http import JsonResponse
from .models import wordcloud, chart, zhihu, connect
import logging


def get_wordcloud(request):
    typeId = request.POST['typeId']
    try:
        obj = wordcloud.objects.filter(typeId=typeId)[0]
        typeId = obj.typeId
        type = obj.type
        content = obj.content
        res = {
            "state": 0,
            "data": {
                "typeId": typeId,
                "type": type,
                "content": content
            }
        }
    except Exception as e:
        logging.warning(e)
        res = {
            'state': 1,
            'data': None
        }

    return JsonResponse(res)


def get_chart(request):
    typeId = request.POST['typeId']
    try:
        obj = chart.objects.filter(typeId=typeId)[0]
        print(obj)
        typeId = obj.typeId
        type = obj.type
        content = obj.content
        res = {
            "state": 0,
            "data": {
                "typeId": typeId,
                "type": type,
                "content": content
            }
        }
    except Exception as e:
        logging.warning(e)
        res = {
            'state': 1,
            'data': None
        }

    return JsonResponse(res)


def get_zhihu(request):
    subtype = request.POST['subtype']
    try:
        obj = zhihu.objects.filter(subtype=subtype)[0]
        typeId = obj.typeId
        type = obj.type
        subtype = obj.subtype
        content = obj.content
        res = {
            "state": 0,
            "data": {
                "typeId": typeId,
                "type": type,
                "subtype": subtype,
                "content": content
            }
        }
    except Exception as e:
        logging.warning(e)
        res = {
            'state': 1,
            'data': None
        }

    return JsonResponse(res)


def get_connect(request):
    param = request.POST['centerword']
    try:
        obj = connect.objects.filter(centerword=param)[0]
        centerword = obj.centerword
        connectwords = obj.connectwords
        sortedList = sorted(connectwords, key=lambda x: 1/x['value'])

        res = {
            "state": 0,
            "data": {
                "centerword": centerword,
                "connectword": sortedList
            }
        }
    except Exception as e:
        logging.warning(e)
        res = {
            'state': 1,
            'data': None
        }

    return JsonResponse(res)
