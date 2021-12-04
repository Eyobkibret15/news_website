from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup

"""
this will scrap the latest news from techcrunch.com news  main site every time 
we called it. we use BeautifulSoup python module and django rest-framework
serialization for the validation of incomming data inorder to store to our database   
"""

# @api_view(["GET", ])
def techcrunch_pages():
    """
    we update the the first 5 latest News from TechCrunch site to our TechCrunch  table
    on our database we we want it
    :return: None
    """
    res = requests.get("https://techcrunch.com/")
    soup = BeautifulSoup(res.text, "html.parser")

    news = soup.find_all(class_='post-block post-block--image post-block--unread')

    newslist = filtering_techcrunch(news)
    data = {}
    t = TechCrunch.objects.all().delete()
    for news in newslist:
        data['title'] = news["title"].replace("'", '"')
        data['title_link'] = news['title_link'].replace("'", '"')
        data['news_time'] = news['time'].replace("'", '"')
        data['author'] = news['author'].replace("'", '"')
        data['detail'] = news['detail'].replace("'", '"')
        tech = TechCrunchSerializer(data=data)
        if tech.is_valid():
            tech.save()
        else:
            pass
    # return Response(status=status.HTTP_201_CREATED)

def filtering_techcrunch(news):
    news_list = []
    for index, item in enumerate(news):
        if (item.find(class_="post-block__header").find("h2").find("a")):
            titles = item.find(class_="post-block__header").find("h2").find("a")
            title = titles.get_text().replace("\n", "").strip()
            title_link = titles.get("href").replace("\n", "").strip()
        if (item.find(class_="post-block__meta").find("a")):
            author = item.find(class_="post-block__meta").find("a").get_text().replace("\n", "").strip()
        if (item.find(class_="post-block__meta").find(class_="river-byline__time")):
            time = item.find(class_="post-block__meta").find(class_="river-byline__time").get_text().replace("\n",
                                                                                                             "").strip()
        if (item.find(class_="post-block__content")):
            detail = item.find(class_="post-block__content").get_text().replace("\n", "").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link, 'time': time, 'author': author,
                            'detail': detail}
            news_list.append(current_news)
        if (len(news_list) > 5):
            return news_list[:5]
    return news_list[:5]
