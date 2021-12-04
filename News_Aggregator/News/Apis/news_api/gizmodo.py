from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup

"""
this will scrap the latest news from gizmodo.com news  main site every time 
we called it. we use BeautifulSoup python module and django rest-framework
serialization for the validation of incoming data inorder to store to our database   
"""

# @api_view(["GET",])
def gizmodo_pages():
    """
    scraping data or the 5 latest and popular news  from gizmodo site to our gizmodo
     table in our database
    :return: None
    """
    res = requests.get("https://gizmodo.com/")
    soup = BeautifulSoup(res.text, "html.parser")

    news = soup.find_all(class_='sc-1pw4fyi-6 egHsIp')

    newslist = filtering_gizmodo(news)
    data = {}
    b = Gizmodo.objects.all().delete()
    for news in newslist:
        data['title'] = news["title"].replace("'", '"')
        data['title_link'] = news['title_link'].replace("'", '"')
        data['time'] = news['time'].replace("'", '"')
        data['author'] = news['author'].replace("'", '"')
        data['author_link'] = news['author_link'].replace("'", '"')
        gizmodo = GizmodoSerializer(data=data)
        if gizmodo.is_valid():
            gizmodo.save()
        else:
            pass

    return Response(data)


def filtering_gizmodo(news):
    news_list = []
    for index, item in enumerate(news):
        if (item.find(class_="sc-1out364-0 hMndXN sc-1pw4fyi-4 coioyN js_link").find("h4").get_text()):
            title = item.find(class_="sc-1out364-0 hMndXN sc-1pw4fyi-4 coioyN js_link").find("h4").get_text().replace("\n", "").strip()
        if (item.find(class_="sc-1out364-0 hMndXN sc-1pw4fyi-4 coioyN js_link").get("href")):
            title_link = item.find(class_="sc-1out364-0 hMndXN sc-1pw4fyi-4 coioyN js_link").get("href").replace("\n", "").strip()
        if (item.find(class_="ysh9pk-0 jjPDwW").find(class_="sc-1out364-0 hMndXN js_link").get_text()):
            author = item.find(class_="ysh9pk-0 jjPDwW").find(class_="sc-1out364-0 hMndXN js_link").get_text().replace("\n", "").strip()
        if (item.find(class_="ysh9pk-0 jjPDwW").find(class_="sc-1out364-0 hMndXN js_link").get("href")):
            author_link = "https://gizmodo.com" + item.find(class_="ysh9pk-0 jjPDwW").find(class_="sc-1out364-0 hMndXN js_link").get("href").replace("\n", "").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link,'time':"",'author_link' : author_link ,
                             'author': author}
            news_list.append(current_news)
        if(len(news_list) > 5):
            return news_list[:5]

    return news_list[:5]
