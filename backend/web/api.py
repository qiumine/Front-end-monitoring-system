import json
from optparse import Values
from urllib import response
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse, JsonResponse
from web.models import BLANKSCREEN, pv, stayTime
from web.models import resourceError,jsError,firstInput,timing,paint,xhr,fetch
from django.forms.models import model_to_dict
import time

#ResourceError
def getResourceError(request):
    obj = resourceError.objects
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : {
            'total' : len(obj.all()),
        }
    }
    return JsonResponse(data=response_dict, safe=True)

def getResourceErrorbyDay(request):
    obj = resourceError.objects
    trend = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = {
                'total' : 1, 
            }
        else:
            trend[format_date]['total'] += 1

    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

def getResourceErrorbyHour(request):
    obj = resourceError.objects
    trend = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        day = time.strftime('%Y-%m-%d', date)
        hour = time.strftime('%H', date)
        if day not in trend:
            trend[day] = {}
            for i in range(24):
                trend[day][str(i).zfill(2)] = 0
        
        trend[day][hour] += 1

    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

#JsError
def getJsError(request):
    obj = jsError.objects
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : {
            'total' : len(obj.all()),
            'jsError' : len(obj.filter(errorType__exact='jsError')), 
            'promiseError' : len(obj.filter(errorType__exact='promiseError'))
        }
    }
    return JsonResponse(data=response_dict, safe=True)
def getJsErrorbyHour(request):
    obj = jsError.objects
    trend = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        day = time.strftime('%Y-%m-%d', date)
        hour = time.strftime('%H', date)
        js = 1 if item.errorType == 'jsError' else 0
        if day not in trend:
            trend[day] = {}
            for i in range(24):
                trend[day][str(i).zfill(2)] = {
                    'total' : 0, 
                    'jsError' : 0,
                    'promiseError' : 0
                }
        trend[day][hour]['total'] += 1
        trend[day][hour]['jsError'] += js
        trend[day][hour]['promiseError'] += 1 - js

    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

def getJsErrorbyDay(request):
    obj = jsError.objects
    trend = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        js = 1 if item.errorType == 'jsError' else 0
        if format_date not in trend:
            trend[format_date] = {
                'total' : 1, 
                'jsError' : js,
                'promiseError' : 1 - js
            }
        else:
            trend[format_date]['total'] += 1
            trend[format_date]['jsError'] += js
            trend[format_date]['promiseError'] += 1 - js

    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

#blank
def getBlank(request):
    row = BLANKSCREEN.objects.last()
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : model_to_dict(row)
    }
    return JsonResponse(data=response_dict, safe=True)

#ApiError
def getApiErrorbyHour(request):
    obj1 = xhr.objects
    obj2 = fetch.objects
    trend = {}
    #xhr trend
    for item in obj1.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        day = time.strftime('%Y-%m-%d', date)
        hour = time.strftime('%H', date)
        if day not in trend:
            trend[day] = {}
            for i in range(24):
                trend[day][str(i).zfill(2)] = {
                    'total' : 0, 
                    'xhr' : {
                        'total' : 0,
                        'error' : 0
                    },
                    'fetch' : {
                        'total' : 0,
                        'error' : 0
                    }
                }
        trend[day][hour]['total'] += 1
        trend[day][hour]['xhr']['total'] += 1
        trend[day][hour]['xhr']['error'] += 1 if item.status != '200-OK' else 0
    #fetch trend
    for item in obj2.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        day = time.strftime('%Y-%m-%d', date)
        hour = time.strftime('%H', date)
        if day not in trend:
            trend[day] = {}
            for i in range(24):
                trend[day][str(i).zfill(2)] = {
                    'total' : 0, 
                    'xhr' : {
                        'total' : 0,
                        'error' : 0
                    },
                    'fetch' : {
                        'total' : 0,
                        'error' : 0
                    }
                }
        trend[day][hour]['total'] += 1
        trend[day][hour]['fetch']['total'] += 1
        trend[day][hour]['fetch']['error'] += 1 if item.success == 'false' else 0
    
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

def getApiErrorbyDay(request):
    obj1 = xhr.objects
    obj2 = fetch.objects
    trend = {}
    #xhr trend
    for item in obj1.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = {
                'total' : 0, 
                'xhr' : {
                    'total' : 0,
                    'error' : 0
                },
                'fetch' : {
                    'total' : 0,
                    'error' : 0
                }
            }
        trend[format_date]['total'] += 1
        trend[format_date]['xhr']['total'] += 1
        trend[format_date]['xhr']['error'] += 1 if item.status != '200-OK' else 0
    #fetch trend
    for item in obj2.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = {
                'total' : 0, 
                'xhr' : {
                    'total' : 0,
                    'error' : 0
                },
                'fetch' : {
                    'total' : 0,
                    'error' : 0
                }
            }
        trend[format_date]['total'] += 1
        trend[format_date]['fetch']['total'] += 1
        trend[format_date]['fetch']['error'] += 1 if item.success == 'false' else 0
    
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

def getApiError(request):
    obj1 = xhr.objects
    obj2 = fetch.objects

    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : {
            'total' : len(obj1.all()),
            'xhr' : {
                'total' : len(obj1.filter(type__exact='xhr')),
                'error' : len(obj1.filter(type__exact='xhr')) - 
                          len(obj1.filter(type__exact='xhr', status__exact='200-OK'))
            },
            'fetch' : {
               'total' : len(obj2.filter(type__exact='fetch')),
               'error' : len(obj2.filter(type__exact='fetch', success__exact='false'))
            }
        }
    }
    return JsonResponse(data=response_dict, safe=True)

#firstInput
def getFirstInputDelay(request):
    row = firstInput.objects.last()
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : model_to_dict(row)
    }
    return JsonResponse(data=response_dict, safe=True)

#time
def getTiming(request):
    row = timing.objects.last()
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : model_to_dict(row)
    }
    return JsonResponse(data=response_dict, safe=True)

#paint
def getFCP(request):
    row = paint.objects.last()
    response_dict = {'code' : 200, 'msg': 'Success!', 'data' : row.firstContentfulPaint }
    return JsonResponse(data=response_dict, safe=True)
def getFMP(request):
    row = paint.objects.last()
    response_dict = {'code' : 200, 'msg': 'Success!', 'data' : row.firstMeaningfulPaint }
    return JsonResponse(data=response_dict, safe=True)
def getFP(request):
    row = paint.objects.last()
    response_dict = {'code' : 200, 'msg': 'Success!', 'data' : row.firstPaint }
    return JsonResponse(data=response_dict, safe=True)
def getLCP(request):
    row = paint.objects.last()
    response_dict = {'code' : 200, 'msg': 'Success!', 'data' : row.largestContentfulPaint }
    return JsonResponse(data=response_dict, safe=True)
def getPaint(request):
    row = paint.objects.last()
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : 
            {
                'firstContentFulPaint' : row.firstContentfulPaint,
                'firstMeaningfulPaint' : row.firstMeaningfulPaint,
                'firstPaint' : row.firstPaint,
                'largestContentfulPaint' : row.largestContentfulPaint
            } 
    }
    return JsonResponse(data=response_dict, safe=True)
#uv

def getMac(x):
    return x.uuid[-12:]
def getUV(request):
    obj = set(map(getMac, list(pv.objects.all())))
    response_dict = {'code' : 200, 'msg': 'Success!', 'data' : len(obj) }
    return JsonResponse(data=response_dict, safe=True)
def getUVbyDay(request):
    obj = pv.objects
    user = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in user:
            user[format_date] = []
        user[format_date].append(getMac(item))
    
    trend = {}
    for key in user.keys():
        trend[key] = len(set(user[key]))
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)
def getUVbyHour(request):
    obj = pv.objects
    user = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        day = time.strftime('%Y-%m-%d', date)
        hour = time.strftime('%H', date)
        if day not in user:
            user[day] = {}
            for i in range(24):
                user[day][str(i).zfill(2)] = []
        user[day][hour].append(getMac(item))
    
    trend = {}
    for day in user.keys():
        trend[day] = {}
        for hour in user[day].keys():
            trend[day][hour] = len(set(user[day][hour]))
    
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

#pv


def getPV(request):
    obj = pv.objects.all()
    response_dict = {'code' : 200, 'msg': 'Success!', 'data' : len(obj) }
    return JsonResponse(data=response_dict, safe=True)
def getPVbyDay(request):
    obj = pv.objects
    trend = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = 0
        trend[format_date] += 1

    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

def getPVbyHour(request):
    obj = pv.objects
    trend = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        day = time.strftime('%Y-%m-%d', date)
        hour = time.strftime('%H', date)
        if day not in trend:
            trend[day] = {}
            for i in range(24):
                trend[day][str(i).zfill(2)] = 0
        
        trend[day][hour] += 1

    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

from statistics import mean
def getStaytime(request):
    obj = stayTime.objects.values_list('stayTime')
    all = list(map(lambda x: int(x[0]), obj))
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : {
            'min' : min(all),
            'max' : max(all),
            'average' : mean(all), 
            'all' : all
        }
    }
    return JsonResponse(data=response_dict, safe=True)