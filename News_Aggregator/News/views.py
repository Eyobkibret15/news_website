import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import *

# Create your views here.\
data = []

"""
OUR MAIN FILE/CONTROLLER 
"""
@api_view(["GET",])
def home(request):
    """
    This is  RESTFULL API to get all the required data from our database
    to the end users /client sides
    :param requests -  recive a request from the end users:
    :return  JSON response , return all the data to our end users :
    """
    home_data = {}
    if request.method == "GET":
        try:
            bbc_queryset = BBC.objects.all()
            collect(bbc_queryset, 'bbc')
            home_data['bbc'] = data
            first_news_queryset = FirstNews.objects.all()
            collect(first_news_queryset, 'first_news')
            home_data['first_news'] = data
            sky_sport_queryset = SkySport.objects.all()
            collect(sky_sport_queryset, 'sky_sport')
            home_data['sky_sport'] = data
            tech_crunch_queryset = TechCrunch.objects.all()
            collect(tech_crunch_queryset, 'tech_crunch')
            home_data['tech_crunch'] = data
            gizmodo_queryset = Gizmodo.objects.all()
            collect(gizmodo_queryset, 'gizmodo')
            home_data['gizmodo'] = data
        except Exception as e:
            print(f'{e} in manin')
            pass
        # home_data = json.dumps(home_data)
    return Response(home_data, status=200)


@api_view(['GET'])
def check(requests: Request):
    """

    :param requests:
    :return:
    """
    # data = '<html><body><h1>I love you baby </h1></body></html>'
    return render(requests, 'index.html')


def collect(obj, name):
    """
    this is just to communicate with our database to get the first 5 news from
    each table 
    :param obj: a queryset object of a model
    :param name:just a string of the table name
    :return: None
    """
    if obj.count() >= 5:
        # print(object[:5])
        coun = 5
    else:
        coun = obj.count()
    global data
    data = []
    for i in range(coun):
        content = {}
        model = obj[i]
        try:
            content['title'] = model.title
            content['title_link'] = model.title_link
            content['detail'] = model.detail
            content['record_time'] = str(model.record_time)
            if name == 'bbc':
                content['news_time'] = str(model.news_time)
                content['location'] = model.location
            elif name == 'first_news':
                content['type'] = model.type
                content['detail_link'] = model.detail_link
            elif name == 'tech_crunch':
                content['news_time'] = str(model.news_time)
                content['author'] = model.author
            elif name == 'gizmodo':
                content['news_time'] = str(model.news_time)
                content['author'] = model.author
                content['author_link'] = model.author_link
            data.append(content)
        except Exception as E:
            print(f"{E} in collecting")
            pass
