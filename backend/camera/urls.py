from django.urls import path
from django.urls import re_path as url
from . import views
urlpatterns = [
    path("",views.getdata,name="getdata"),
]