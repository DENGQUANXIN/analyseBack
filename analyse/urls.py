from .views import get_wordcloud, get_chart, get_zhihu, get_connect
from django.urls import path

urlpatterns = [
    path('wordcloud', get_wordcloud),
    path('chart', get_chart),
    path('zhihu', get_zhihu),
    path('connect', get_connect)
]
