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
    #resourceError
    url(r'^getResourceError/$', api.getResourceError, name='getResourceError'),
    url(r'^getResourceErrorbyDay/$', api.getResourceErrorbyDay, name='getResourceErrorbyDay'),
    url(r'^getResourceErrorbyHour/$', api.getResourceErrorbyHour, name='getResourceErrorbyHour'),
    #jserror
    url(r'^getJsError/$', api.getJsError, name='getJsError'),
    url(r'^getJsErrorbyDay/$', api.getJsErrorbyDay, name='getJsErrorbyDay'),
    url(r'^getJsErrorbyHour/$', api.getJsErrorbyHour, name='getJsErrorbyHour'),
    #Blank
    url(r'^getBlank/$', api.getBlank, name='getBlank'),
    #ApiError
    url(r'^getApiError/$', api.getApiError, name='getApiError'),
    url(r'^getApiErrorbyDay/$', api.getApiErrorbyDay, name='getApiErrorbyDay'),
    url(r'^getApiErrorbyHour/$', api.getApiErrorbyHour, name='getApiErrorbyHour'),
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
    #pv
    url(r'^getPV/$', api.getPV, name='getPV'),
    url(r'^getPVbyDay/$', api.getPVbyDay, name='getPVbyDay'),
    url(r'^getPVbyHour/$', api.getPVbyHour, name='getPVbyHour'),
    #uv
    url(r'^getUV/$', api.getUV, name='getUV'),
    url(r'^getUVbyDay/$', api.getUVbyDay, name='getUVbyDay'),
    url(r'^getUVbyHour/$', api.getUVbyHour, name='getUVbyHour'),
    #staytime
    url(r'^getStaytime/$', api.getStaytime, name='getStaytime'),
]
