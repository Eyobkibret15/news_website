from apscheduler.schedulers.background import BackgroundScheduler
from .Apis.news_api import bbc , gizmodo , techcrunch ,skysport , the_first_news

""" 
THIS WILL ALLOW US TO UPDATE OUR DATABASE BASED ON OUR NEEDS
THE TIME INTERVAL WE HAVE GIVEN TO , FOR THIS PROJECT WE UPDATE OUR DATABASE IN EVERY 10 MINUTES 
SO THAT OUR CUSTOMERS GET THEIR BEST OF NEWS FREQUENTLY 
"""
scheduler = BackgroundScheduler()
scheduler.add_job(bbc.bbc_pages, 'interval', minutes=10)
scheduler.add_job(gizmodo.gizmodo_pages, 'interval', minutes=10)
scheduler.add_job(techcrunch.techcrunch_pages, 'interval', minutes=10)
scheduler.add_job(skysport.skysport_pages, 'interval', minutes=10)
scheduler.add_job(the_first_news.first_news_pages, 'interval', minutes=10)

try:
    scheduler.start()
except Exception:
    pass