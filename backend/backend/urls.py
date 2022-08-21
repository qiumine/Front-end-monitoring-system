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
    url(r'^getBlank/$', api.getBlank, name='getBlank'),
    url(r'^getApiError/$', api.getApiError, name='getApiError'),
    #firstInput
    url(r'^getFirstInputDelay/$', api.getFirstInputDelay, name='getFirstInputDelay'),
    #time
    url(r'^getTiming/$', api.getTiming, name='getTiming'),
    #paint
    url(r'^getPaint/$', api.getPaint, name='getPaint'),
    url(r'^getFCP/$', api.getFCP, name='getFCP'),
    url(r'^getFP/$', api.getFP, name='getFP'),
    url(r'^getLCP/$', api.getLCP, name='getLCP'),
    url(r'^getFMP/$', api.getFMP, name='getFMP'),
]
