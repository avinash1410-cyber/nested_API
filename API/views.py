from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response


from .models import *
from .serializers import *

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("super30")
        else:
            return render(request,"API/login.html",{
                "message":"Invalid Credentials"
            })
    return render(request,"API/login.html")


def logout_page(request):
    logout(request)
    return render(request,'API/login.html',{
        'message':"Logged out"
    })


class super30(APIView):
    @method_decorator(login_required(login_url='login'))
    def get(self,*args,**kwargs):
        data = city_weather.objects.all()
        serializer = City_weather_srlzr(data, many=True)
        return Response(serializer.data)