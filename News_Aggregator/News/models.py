from django.db import models

"""
 CONFIGURE AND SETUP THE NEWS DATABASE TABLES
 STRUCTURE  
 """


# Create your models here.
class NEWS(models.Model):
    """
    THE IS ABSTRACT OR  BASE TABLE FOR ALL TABLES  ON OUR MODELS
    """
    id = models.AutoField(primary_key=True, verbose_name="news id")
    title = models.CharField(unique=True, max_length=1000, blank=True, null=True)
    title_link = models.URLField(max_length=1000, blank=True, null=True)
    # comment = models.CharField(max_length=1000, blank=True, null=True)
    # comment_link = models.URLField(max_length=1000, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    record_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class HackerNews(NEWS):
    class Meta:
        verbose_name = "Hacker News"
        verbose_name_plural = " Hacker News"


class BBC(NEWS):
    """
    BBC TABLE IT IS A CHILD CLASS FROM PARENT  BASE  CLASS TABLE
    """
    news_time = models.CharField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "BBC News"
        verbose_name_plural = "     BBC News"
        ordering = ['-record_time']


class TheGuardian(NEWS):
    class Meta:
        verbose_name = "The Guardian News"
        verbose_name_plural = "The Guardian News"


class CNN(NEWS):
    class Meta:
        verbose_name = "CNN News"
        verbose_name_plural = "    CNN News"


class SkySport(NEWS):
    """
     SKY SPORT TABLE IT IS A CHILD CLASS FROM PARENT  BASE  CLASS TABLE
    """
    class Meta:
        verbose_name = "Sky Sports News"
        verbose_name_plural = "   Sky Sports News"


class Art(NEWS):
    class Meta:
        verbose_name = "Art News"
        verbose_name_plural = "Art News"


class TVN24(NEWS):
    news_time = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "TVN24 News"
        verbose_name_plural = "TVN24 News"


class Aljazeera(NEWS):
    news_time = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "Aljazeera News"
        verbose_name_plural = "Aljazeera News"


class FirstNews(NEWS):
    """
     FIRST NEWS TABLE IT IS A CHILD CLASS FROM PARENT  BASE  CLASS TABLE
    """
    type = models.CharField(max_length=400, blank=True, null=True)
    detail_link = models.URLField(max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = "First News"
        verbose_name_plural = " First News"


class TechCrunch(NEWS):
    """
     TECCRUNCH TABLE IT IS A CHILD CLASS FROM PARENT  BASE  CLASS TABLE
    """
    news_time = models.CharField(max_length=1000, blank=True, null=True)
    author = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = "TechCrunch News"
        verbose_name_plural = " TechCrunch News"


class Gizmodo(NEWS):
    """
     TGIZMODO TABLE IT IS A CHILD CLASS FROM PARENT  BASE  CLASS TABLE
    """
    news_time = models.CharField(max_length=1000, blank=True, null=True)
    author = models.CharField(max_length=300, null=True, blank=True)
    author_link = models.URLField(max_length=300, null=True, blank=True)

    class Meta:
        verbose_name = "Gizmodo News"
        verbose_name_plural = "Gizmodo News"
