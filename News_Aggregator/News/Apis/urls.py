from django.urls import path
from .news_api import *
from .news_api.bbc import bbc_pages
from .news_api.hackernews import hackernews_pages
from .news_api.cnn import cnn_page
from .news_api.skysport import skysport_pages
from .news_api.techcrunch import techcrunch_pages
from .news_api.the_first_news import first_news_pages
from .news_api.artnews import artnewspaper_page
from .news_api.aljazeera import aljazeera_page
from .news_api.gizmodo import gizmodo_pages
"""
under development to check if the apis are working correctly 
contains specifically api urls
"""
urlpatterns = [
    path('api/hackernews/' , hackernews_pages , name="hacker"),
    path('api/cnn/', cnn_page, name="cnn"),
    path('api/bbc/', bbc_pages, name="bbc") ,
    path('api/sky-sport/', skysport_pages, name="sky_sport"),
    path('api/tech-crunch/', techcrunch_pages, name="tech_crunch"),
    path('api/first-news/', first_news_pages, name="first_news"),
    path('api/art/', artnewspaper_page, name="art"),
    path('api/aljazera/', aljazeera_page, name="aljazera"),
    path('api/gizmodo/', gizmodo_pages, name="gizmodo"),
]