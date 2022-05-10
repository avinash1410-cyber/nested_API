from django.urls import path,include
from .views import super30,login_page,logout

urlpatterns = [
    path('',super30.as_view(),name="super30"),
    path('login/',login_page,name="login"),
    path('logout/',logout,name="logout"),
]