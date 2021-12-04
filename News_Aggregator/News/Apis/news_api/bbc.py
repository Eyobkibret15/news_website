import re
from News.serializers import *
from News.models import *
import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
"""
this will scrap the latest news from bbc.com news  main site every time 
we called it. we use BeautifulSoup python module and django rest-framework
serialization for the validation of incomming data inorder to store to our database   
"""

# @api_view(["GET",])
# from serializers import BBCSerializer
def bbc_pages():
    """
    this function will update the BBC table on the database
    :return: None
    """
    res = requests.get("https://www.bbc.com/news")
    soup = BeautifulSoup(res.text, "html.parser")
    grn = soup.find_all("a")
    stitle = soup.find_all(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold "
                                  "nw-o-link-split__anchor")
    ftitle = soup.find_all(class_="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold "
                                  "nw-o-link-split__anchor")
    title = ftitle + stitle
    summary = soup.find_all(class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")
    date = soup.find_all(class_="gs-o-bullet__text date qa-status-date gs-u-align-middle gs-u-display-inline")
    area = soup.find_all(class_="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link "
                                "nw-o-link--no-visited-state")
    news_list = (filtering_bbc_news(title, summary, date, area))
    data = {}
    b = BBC.objects.all().delete()
    for news in news_list:
        data['title'] = news["title"].replace("'", '"')
        data['title_link'] = news['title_link'].replace("'", '"')
        data['news_time'] = news['time'].replace("'", '"')
        data['location'] = news['location'].replace("'", '"')
        data['detail'] = news['detail'].replace("'", '"')
        bbc = BBCSerializer(data=data)
        if bbc.is_valid():
            bbc.save()
        else:
            pass
    # return Response(status=status.HTTP_201_CREATED)

def filtering_bbc_news(title, summary, date, area):
    news_list = []
    for index, item in enumerate(title[:8]):
        title = item.getText()
        url = "https://www.bbc.com" + item.get("href")
        time = re.split("h|m|day",date[index].getText(),1)[1]
        detail = summary[index].getText()
        location = area[index].getText()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': url, 'time': time,
                            'location': location, 'detail': detail}
            news_list.append(current_news)
        if(len(news_list) > 5):
            return news_list[:5]

    return news_list[:5]