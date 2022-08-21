import json
from urllib import response
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse, JsonResponse
from web.models import BLANKSCREEN
from web.models import resourceError,jsError,firstInput,timing,paint,xhr
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
        format_date = time.strftime('%Y-%m-%d %H', date)
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
        format_date = time.strftime('%Y-%m-%d %H', date)
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
    #obj2 = fetch.objects
    trend = {}
    #xhr trend
    for item in obj1.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d %H', date)
        if format_date not in trend:
            trend[format_date] = {
                'total' : 1, 
                'xhr' : {
                    'total' : 1,
                    'error' : 1 if item.status != '200-OK' else 0
                },
                'fetch' : {
                    'total' : 0,
                    'error' : 0
                }
            }
        else:
            trend[format_date]['total'] += 1
            trend[format_date]['xhr']['total'] += 1
            trend[format_date]['xhr']['error'] += 1 if item.status != '200-OK' else 0
    #fetch trend
    """
    for item in obj2.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = {
                'total' : 1, 
                'xhr' : {
                    'total' : 0,
                    'error' : 0
                },
                'fetch' : {
                    'total' : 1,
                    'error' : 1 if item.success == 'false' else 0
                }
            }
        else:
            trend[format_date]['total'] += 1
            trend[format_date]['fetch']['total'] += 1
            trend[format_date]['fetch']['error'] += 1 if item.success == 'false' else 0
    """
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

def getApiErrorbyDay(request):
    obj1 = xhr.objects
    #obj2 = fetch.objects
    trend = {}
    #xhr trend
    for item in obj1.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = {
                'total' : 1, 
                'xhr' : {
                    'total' : 1,
                    'error' : 1 if item.status != '200-OK' else 0
                },
                'fetch' : {
                    'total' : 0,
                    'error' : 0
                }
            }
        else:
            trend[format_date]['total'] += 1
            trend[format_date]['xhr']['total'] += 1
            trend[format_date]['xhr']['error'] += 1 if item.status != '200-OK' else 0
    #fetch trend
    """
    for item in obj2.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = {
                'total' : 1, 
                'xhr' : {
                    'total' : 0,
                    'error' : 0
                },
                'fetch' : {
                    'total' : 1,
                    'error' : 1 if item.success == 'false' else 0
                }
            }
        else:
            trend[format_date]['total'] += 1
            trend[format_date]['fetch']['total'] += 1
            trend[format_date]['fetch']['error'] += 1 if item.success == 'false' else 0
    """
    response_dict = {
        'code' : 200, 
        'msg': 'Success!', 
        'data' : trend
    }
    return JsonResponse(data=response_dict, safe=True)

def getApiError(request):
    obj1 = xhr.objects
    #obj2 = fetch.objects

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
            #'fetch' : {
            #    'total' : len(obj2.filter(type__exact='fetch')),
            #    'error' : len(obj2.filter(type__exact='fetch', success__exact='false'))
            #}
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

