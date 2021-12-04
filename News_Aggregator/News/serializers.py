from rest_framework.serializers import ModelSerializer
from .models import *
"""
MODEL SERIALIZER WITH THE HELP OF DJANGO RESTFRAMEWORK 
IT HALPS US TO VALIDATE DATA BEFORE WE STORE TO OUR DATABASE 
"""
class HackerSerializer(ModelSerializer):
    class Meta:
        model = HackerNews
        fields = '__all__'


class BBCSerializer(ModelSerializer):
    """
    BBC SERIALIZER CLASS
    """
    class Meta:
        model = BBC
        fields = '__all__'


class TheGuardianSerializer(ModelSerializer):
    class Meta:
        model = TheGuardian
        fields = '__all__'


class CNNSerializer(ModelSerializer):
    class Meta:
        model = CNN
        fields = '__all__'


class SkySportSerializer(ModelSerializer):
    """
        SKY SPORT SERIALIZER CLASS
    """
    class Meta:
        model = SkySport
        fields = '__all__'


class ArtSerializer(ModelSerializer):
    class Meta:
        model = Art
        fields = '__all__'


class TVN24Serializer(ModelSerializer):
    class Meta:
        model = TVN24
        fields = '__all__'


class AljazeeraSerializer(ModelSerializer):
    class Meta:
        model = Aljazeera
        fields = '__all__'


class FirstNewsSerializer(ModelSerializer):
    """
        FIRST NEWS SERIALIZER CLASS
    """
    class Meta:
        model = FirstNews
        fields = '__all__'


class TechCrunchSerializer(ModelSerializer):
    """
        TECHCRUNCH SERIALIZER CLASS
    """
    class Meta:
        model = TechCrunch
        fields = '__all__'


class GizmodoSerializer(ModelSerializer):
    """
        GIZMODO SERIALIZER CLASS
    """
    class Meta:
        model = Gizmodo
        fields = '__all__'
