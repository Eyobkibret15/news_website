import re

from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request



@api_view(['GET',])
def aljazeera_page(request):
    res = requests.get("https://www.aljazeera.com/")
    soup = BeautifulSoup(res.text, "html.parser")

    htitle = soup.find_all(class_='fte-featured__title__link')
    stitle = soup.find_all(class_='fte-featured__excerpt__link fte-featured__title__link')
    title = htitle + stitle

    details = soup.find_all('p')
    newslist = filtering_aljazeera_news(title ,details)
    data = {}
    for news in newslist:
        data['title'] = news["title"].replace("'", '"')
        data['title_link']=news['title_link'].replace("'", '"')
        data['time'] = news['time'].replace("'", '"')
        data['detail_link'] = news['detaillink'].replace("'", '"')
        data['detail'] = news['detail'].replace("'", '"')
        aljazeera = AljazeeraSerializer(data=data)
        # print("00000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        if aljazeera.is_valid():
            # print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111")
            # b = BBC.objects.all().delete()
            # print(b)
            aljazeera.save()
        else:
            pass
    # database.insert_into_database("aljazeera", title, titlelink, time, detaillink, detail)

    return Response(data)


def filtering_aljazeera_news(title, summery):
    news_list = []
    for index, item in enumerate(title[:8]):
        title = item.get_text()
        title_link = "https://www.aljazeera.com" + item.get('href')

        detail = summery[index].get_text()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link , 'time':"",'detaillink':title_link ,'detail': detail }
            news_list.append(current_news)
        if(len(news_list) > 5):
            return news_list[:5]

    return news_list[:5]

