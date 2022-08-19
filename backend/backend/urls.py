"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from camera import views
from web import api

urlpatterns = [
    url(r'^senddata/$', views.getdata, name='senddata'),
    url(r'^get_resourceError/$', api.get_resourceError, name='get_resourceError'),
    url(r'^get_jsError/$', api.get_jsError, name='get_jsError'),
    url(r'^get_blank/$', api.get_blank, name='get_blank'),
    url(r'^get_xhr/$', api.get_xhr, name='get_xhr'),
    url(r'^get_firstInputDelay/$', api.get_firstInputDelay, name='get_firstInputDelay'),
    url(r'^get_timing/$', api.get_timing, name='get_timing'),
    url(r'^get_paint/$', api.get_paint, name='get_paint'),
]
