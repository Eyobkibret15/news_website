from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup

"""
this will scrap the latest news from skysport.com news  main site every time 
we called it. we use BeautifulSoup python module and django rest-framework
serialization for the validation of incomming data inorder to store to our database   
"""

# @api_view(["GET",])
def skysport_pages():
    """
    this will store 5 latest news to our sky sport table in our database based
    on our needs
    :return:
    """
    res = requests.get("https://www.skysports.com/")
    soup = BeautifulSoup(res.text, "html.parser")
    titles = soup.find_all("h3",class_="sdc-site-tile__headline")
    newslist = (filtering_skysport_news(titles))
    data = {}
    SkySport.objects.all().delete()
    for news in newslist:
        data['title'] = news["title"].replace("'", '"')
        data['title_link'] = news['title_link'].replace("'", '"')
        data['comment'] = news['comment'].replace("'", '"')
        data['comment_link'] = news['comment_link'].replace("'", '"')
        data['detail'] = news['detail'].replace("'", '"')
        sky = SkySportSerializer(data=data)
        # print(data)
        if sky.is_valid():
           sky.save()
        else:
            pass
    return Response(data,status=status.HTTP_201_CREATED)

def filtering_skysport_news(titles):
    news_list = []
    for index, item in enumerate(titles):
        if (item.find("a").get_text()):
            title = item.find("a").get_text().replace("\n", "").strip()
        if (item.find("a").get("href")):
            title_link = "https://www.skysports.com" + item.find("a").get("href").replace("\n", "").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link, 'comment': "", 'comment_link': "",
                            'detail': ""}
            news_list.append(current_news)
        if (len(news_list) > 5):
            return news_list[:5]