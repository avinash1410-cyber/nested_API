from django.db import models

# Create your models here.
class Weather(models.Model):
    main=models.CharField(max_length=100,default="Clear")
    description=models.CharField(max_length=100,default="Clear Sky")
    icon=models.ImageField(null=True,blank=True)


class City(models.Model):
    lat=models.CharField(max_length=100,null=True,blank=True)
    lon=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    timeZone=models.CharField(max_length=100,null=True,blank=True)

class Main(models.Model):
    temp=models.IntegerField(null=True,blank=True)
    feels_like=models.IntegerField(null=True,blank=True)
    temp_min=models.IntegerField(null=True,blank=True)
    temp_max=models.IntegerField(null=True,blank=True)
    pressure=models.IntegerField(null=True,blank=True)
    humidity=models.IntegerField(null=True,blank=True)


class Wind(models.Model):
    speed=models.IntegerField(null=True,blank=True)
    deg=models.IntegerField(null=True,blank=True)


class Clouds(models.Model):
    all=models.IntegerField(null=True,blank=True)


class sys(models.Model):
    type=models.IntegerField(null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    sunrise=models.CharField(max_length=100,null=True,blank=True)
    sunset=models.CharField(max_length=100,null=True,blank=True)



class city_weather(models.Model):
    City=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    Weather=models.ForeignKey(Weather,on_delete=models.CASCADE,null=True,blank=True)
    sys=models.ForeignKey(sys,on_delete=models.CASCADE,null=True,blank=True)
    Clouds=models.ForeignKey(Clouds,on_delete=models.CASCADE,null=True,blank=True)
    Wind=models.ForeignKey(Wind,on_delete=models.CASCADE,null=True,blank=True)
    Main=models.ForeignKey(Main,on_delete=models.CASCADE,null=True,blank=True)
    visibility=models.IntegerField(default=1000,null=True,blank=True)
    view=models.CharField(max_length=200,null=True,blank=True)
    cod=models.IntegerField(null=True,blank=True)
    base=models.CharField(max_length=100,null=True,blank=True)
    dt=models.CharField(max_length=100,null=True,blank=True)