from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from News.serializers import *
import requests
from bs4 import BeautifulSoup


@api_view(["GET", "POST"])
def hackernews_pages(request:Request):
    res = requests.get("https://news.ycombinator.com/news")
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.select(".storylink")
    vote = soup.select(".subtext")
    news_list = []
    for index, item in enumerate(title):
        url = title[index].get("href")
        point = vote[index].find(class_="score")
        comment = vote[index].find(class_="age")
        comment_link = "https://news.ycombinator.com/" + comment.find('a', href=True).get("href")
        comment = vote[index].getText().split("ago", 1)[1].replace("\xa0", " ").replace("  | hide |", "")
        detail = vote[index].getText().replace("| hide |", "").replace("\n", "").split("ago", 1)[0] + "ago"
        if point:
            current_vote = int(point.getText().replace(" points", ""))
            if current_vote > 99:
                current_news = {'Title': item.getText(), 'title_link': url, 'Vote': point.getText(),
                                'comments_link': comment_link, 'detail': detail, 'comment': comment}
                news_list.append(current_news)
    news_list = sorted(news_list[:5], key=lambda k: k['Vote'])
    data = {}
    print(news_list)
    for news in news_list:
        data['title'] = news["Title"].replace("'", '"')
        data['titlelink']= news['title_link'].replace("'", '"')
        data['comment'] =news['comment'].replace("'", '"')
        data['commentlink'] = news['comments_link'].replace("'", '"')
        data['detail']=news['detail'].replace("'", '"')
        print("000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        hacker = HackerSerializer(data=data)
        if hacker.is_valid():
            print("11111111111111111111111111111111111111111111111111111111111")
            hacker.save()
        else:
            pass
    return Response(data,status=status.HTTP_201_CREATED)

def filtering_hacker_news(title, vote):
    news_list = []
    for index, item in enumerate(title):
        url = title[index].get("href")
        point = vote[index].find(class_="score")
        comment = vote[index].find(class_="age")
        comment_link = "https://news.ycombinator.com/" + comment.find('a', href=True).get("href")
        comment = vote[index].getText().split("ago", 1)[1].replace("\xa0", " ").replace("  | hide |", "")
        detail = vote[index].getText().replace("| hide |", "").replace("\n", "").split("ago", 1)[0] + "ago"
        if point:
            current_vote = int(point.getText().replace(" points", ""))
            if current_vote > 99:
                current_news = {'Title': item.getText(), 'title_link': url, 'Vote': point.getText(),
                                'comments_link': comment_link, 'detail': detail, 'comment': comment}
                news_list.append(current_news)
        if (len(news_list) > 5):
            return sorted(news_list[:5], key=lambda k: k['Vote'])
    return sorted(news_list[:5], key=lambda k: k['Vote'])
