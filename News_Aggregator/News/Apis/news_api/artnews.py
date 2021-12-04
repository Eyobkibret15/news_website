from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup
@api_view(['GET',])
def artnewspaper_page(request):
    res = requests.get("https://www.theartnewspaper.com/")
    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.find_all("a", class_="cp-link")

    newslist = (filtering_artnewspaper(titles))
    data = {}
    print(titles)
    for news in newslist:
        data['title'] = news["title"].replace("'", '"')
        data['title_link'] = news['title_link'].replace("'", '"')
        data['comment'] = news['comment'].replace("'", '"')
        data['comment_link'] = news['comment_link'].replace("'", '"')
        data['detail'] = news['detail'].replace("'", '"')
        art = ArtSerializer(data=data)
        # c = CNN.objects.all().delete()
        # print( CNN.objects.all())
        # print(c)
        # print("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        if art.is_valid():
            # print("222222222222222")

            art.save()
        else:
            pass
    return Response(data, status=status.HTTP_201_CREATED)


def filtering_artnewspaper(titles):
    news_list = []
    for index, item in enumerate(titles):
        if (item.get_text()):
            title = item.get_text().replace("\n", "").strip()
        if (item.get("href")):
            title_link = "https://www.theartnewspaper.com" + item.get("href").replace("\n", "").strip()

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
    return news_list[:5]