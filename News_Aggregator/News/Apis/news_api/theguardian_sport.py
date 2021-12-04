
import database
import requests
from bs4 import BeautifulSoup


def scraping_theguardian_sport_pages():
    res = requests.get("https://www.theguardian.com/international")
    soup = BeautifulSoup(res.text, "html.parser")

    titles = soup.find_all(class_="fc-item__container")

    newslist = (filtering_theguardian_sport_news(titles))

    title =[]
    titlelink =[]
    comment =[]
    commentlink =[]
    detail = []
    for news in newslist:
        title.append(news["title"].replace("'", '"'))
        titlelink.append(news['title_link'].replace("'", '"'))
        comment.append(news['comment'].replace("'", '"'))
        commentlink.append(news['comment_link'].replace("'", '"'))
        detail.append(news['detail'].replace("'", '"'))
    database.insert_into_database("theguardian",title,titlelink,comment,commentlink,detail)
    return "insert to theguardian_sport news"


def filtering_theguardian_sport_news(titles):
    news_list = []
    for index, item in enumerate(titles):
        if (item.find('a').get_text()):
            title =item.find('a').get_text().replace("\n", "").strip()
        if (item.find('a').get('href')):
            title_link = item.find('a').get('href').replace("\n" ,"").strip()

        match_found = 0
        for tit in news_list:
            header = tit["title"]
            if header == title:
                match_found = 1
                continue
        if match_found == 0:
            current_news = {'title': title, 'title_link': title_link, 'comment':"" , 'comment_link':"",
                            'detail':""}
            news_list.append(current_news)
        if (len(news_list) > 5):
            return news_list[:5]