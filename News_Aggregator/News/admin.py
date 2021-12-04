from django.contrib import admin

# Register your models here.


""" 
THIS is controlling our Administration front end for Managment purpose we can
see and what is happening on our backend and data  
"""
from django.apps import apps
from .models import *

models = apps.get_models()

@admin.register(BBC)
class BBCAdmin(admin.ModelAdmin):
    """
    BBC TABLE ADMIN PANNEL.
    """
    readonly_fields = ["record_time"]

@admin.register(SkySport)
class SkySportAdmin(admin.ModelAdmin):
    """
    SKY SPORT ADMIN PANNEL.
    """
    readonly_fields = ["record_time"]


@admin.register(FirstNews)
class FirstNewsAdmin(admin.ModelAdmin):
    """
    FIRST NEWS ADMIN PANNEL.
    """
    readonly_fields = ["record_time"]


@admin.register(TechCrunch)
class TechCrunchAdmin(admin.ModelAdmin):
    """
    TECH CRUNCH ADMIN PANNEL.
    """
    readonly_fields = ["record_time"]

@admin.register(Gizmodo)
class GizmodoAdmin(admin.ModelAdmin):
    """
    GIZMODO ADMIN PANNEL.
    """
    readonly_fields = ["record_time"]
