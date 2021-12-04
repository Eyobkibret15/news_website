from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup

"""
this will scrap the latest news from thefirstnewa.com news  main site every time 
we called it. we use BeautifulSoup python module and django rest-framework
serialization for the validation of incoming data inorder to store to our database   
"""

# @api_view(["GET", ])
def first_news_pages():
    """
    this function will update the first news table in our database based on our needs
    :return:None
    """
    res = requests.get("https://www.thefirstnews.com/")
    soup = BeautifulSoup(res.text, "html.parser")
    titles = soup.find_all(class_='news__item')
    newslist = filtering_first_news(titles)
    data = {}
    f = FirstNews.objects.all().delete()
    for news in newslist:
        data['title'] = news["title"].replace("'", '"')
        data['title_link'] = news['title_link'].replace("'", '"')
        data['type'] = news['type'].replace("'", '"')
        data['detail_link'] = news['detaillink'].replace("'", '"')
        data['detail'] = news['detail'].replace("'", '"')
        first = FirstNewsSerializer(data=data)
        if first.is_valid():
            first.save()
        else:
            pass
    # return Response(status=status.HTTP_201_CREATED)


def filtering_first_news(titles):
    news_list = []
    for index, item in enumerate(titles):
        if (item.find('h3')):
            title = item.find('h3').get_text().replace("\n", "").strip()
        if (item.find('h3').find('a').get('href')):
            title_link = 'https://www.thefirstnews.com' + item.find('h3').find('a').get('href').replace("\n",
                                                                                                        "").strip()
        if (item.find('p')):
            detail = item.find('p').get_text().replace("\n", "").strip()
        if (item.find('span')):
            type = item.find('span').get_text().replace("\n", "").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link, 'type': type, 'detaillink': title_link,
                            'detail': detail}
            news_list.append(current_news)
        if (len(news_list) > 5):
            return news_list[:5]

    return news_list[:5]
