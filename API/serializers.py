from rest_framework import serializers
from .models import *

class Citysrlzr(serializers.ModelSerializer):
    class Meta:
        model=City
        fields="__all__"

class Mainsrlzr(serializers.ModelSerializer):
    class Meta:
        model=Main
        fields="__all__"

class Weathersrlzr(serializers.ModelSerializer):
    class Meta:
        model=Weather
        fields="__all__"
class Syssrlzr(serializers.ModelSerializer):
    class Meta:
        model=sys
        fields="__all__"

class Cloudssrlzr(serializers.ModelSerializer):
    class Meta:
        model=Clouds
        fields="__all__"
class Windsrlzr(serializers.ModelSerializer):
    class Meta:
        model=Wind
        fields="__all__"




class City_weather_srlzr(serializers.ModelSerializer):
    Main = Mainsrlzr(many=False)
    Wind=Windsrlzr()
    Clouds=Cloudssrlzr()
    sys=Syssrlzr()
    Weather=Weathersrlzr()
    City=Citysrlzr()
    class Meta:
        model=city_weather
        fields="__all__"