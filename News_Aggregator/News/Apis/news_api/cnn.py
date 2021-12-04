from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup

@api_view(["GET",])
def cnn_page(request):
    res = requests.get("https://edition.cnn.com/world")
    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.find_all(class_="cd__wrapper")
    # print(titles)
    newslist = (filtering_cnn_news(titles))
    data = {}
    for news in newslist:
        data['title'] = news["title"].replace("'", '"')
        data['title_link'] = news['title_link'].replace("'", '"')
        data['comment'] = news['comment'].replace("'", '"')
        data['comment_link'] = news['comment_link'].replace("'", '"')
        data['detail'] = news['detail'].replace("'", '"')
        cnn = CNNSerializer(data=data)
        # c = CNN.objects.all().delete()
        # print( CNN.objects.all())
        # print(c)
        # print("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        if cnn.is_valid():
            # print("222222222222222")

            cnn.save()
        else:
            pass
    return Response(data,status=status.HTTP_201_CREATED)


def filtering_cnn_news(titles):
    news_list = []
    title = ''
    title_link = ''
    for index, item in enumerate(titles):
        if (item.find("h3").get_text()):
            title = item.find("h3").get_text().replace("\n", "").strip()
        if (item.find("h3").find("a").get("href")):
            title_link = "https://edition.cnn.com" + item.find("h3").find("a").get("href").replace("\n", "").strip()

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
