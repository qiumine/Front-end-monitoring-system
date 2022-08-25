from heapq import merge
from django.http import JsonResponse
from web.models import BLANKSCREEN, pv, stayTime
from web.models import resourceError,jsError,firstInput,timing,paint,xhr,fetch
import time

from statistics import mean

#Errors
def getErrors(request):
    obj = BLANKSCREEN.objects
    data = 0
    for item in obj.all():
        if int(item.emptyPoints) > 16:
            data += 1
    response = [
        {'type' : 'resource error', 'value' : len(resourceError.objects.all())},
        {'type' : 'js error', 'value' : len(jsError.objects.filter(errorType__exact='jsError'))},
        {'type' : 'promise error', 'value' : len(jsError.objects.filter(errorType__exact='promiseError'))},
        {'type' : 'xhr error', 'value' : len(xhr.objects.all()) - len(xhr.objects.filter(status__exact='200-OK'))},
        {'type' : 'fetch error', 'value' : len(fetch.objects.filter(success__exact='False'))},
        {'type' : 'blank error', 'value' : data}
    ]
    return JsonResponse(data={'data': response}, safe=True)

#ResourceError
def getResourceError(request):
    obj = resourceError.objects
    response_dict = {
        'data' : len(obj.all()),
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
            trend[format_date] = 1
        else:
            trend[format_date] += 1
    
    response = []
    for key, value in trend.items():
        response.append({'date': key, 'value': value})
    
    return JsonResponse(data={'data': response}, safe=True)

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
    
    response = []
    for day, hours in trend.items():
        item = {'date' : day, 'data' : []}
        for hour, value in hours.items():
            item['data'].append({'hour' : hour + ':00', 'value' : value})
        response.append(item)

    return JsonResponse(data={'data': response}, safe=True)

def getResourceErrorInfo(request): 
    obj = resourceError.objects.values_list('errorType', 'filename', 'timestamp')
    response = []
    for item in obj:
        timestamp = item[2]
        date = time.localtime(int(timestamp) / 1000)
        t = time.strftime('%Y-%m-%d %H:%M:%S', date)
        response.append( {'time' : t, 'type': item[0], 'message' : item[1]} )
    return JsonResponse(data={'data': list(reversed(response))}, safe=True)

#JsError
def getJsError(request):
    obj = jsError.objects
    response_dict = {
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
    
    response = []
    for day, hours in trend.items():
        item = {'date' : day, 'data' : []}
        for hour, value in hours.items():
            item['data'].append({'hour': hour + ':00', **value})
        response.append(item)

    return JsonResponse(data={'data': response}, safe=True)

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

    response = []
    for key, data in trend.items():
        for kind, value in data.items():
            response.append({'date': key, 'kind': kind, 'value': value})

    return JsonResponse(data={'data' : response}, safe=True)

def getJsErrorInfo(request): 
    obj = jsError.objects.values_list('errorType', 'message', 'stack', 'timestamp')
    response = []
    for item in obj:
        timestamp = item[3]
        date = time.localtime(int(timestamp) / 1000)
        t = time.strftime('%Y-%m-%d %H:%M:%S', date)
        response.append( {'time': t, 'type' : item[0], 'message' : item[1], 'stack' : item[2]})
    return JsonResponse(data={'data': list(reversed(response))}, safe=True)

#blank
def getBlank(request):
    obj = BLANKSCREEN.objects
    data = 0
    for item in obj.all():
        if int(item.emptyPoints) > 16:
            data += 1
    response_dict = {
        'data' : data,
    }
    return JsonResponse(data=response_dict, safe=True)

def getBlankbyDay(request):
    obj = BLANKSCREEN.objects
    trend = {}
    for item in obj.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = 0
        
        trend[format_date] += int(int(item.emptyPoints) > 16)

    response = []
    for key, value in trend.items():
        response.append({'date': key, 'value': value})
    
    return JsonResponse(data={'data': response}, safe=True)

def getBlankbyHour(request):
    obj = BLANKSCREEN.objects
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
        
        trend[day][hour] += int(int(item.emptyPoints) > 16)
    
    response = []
    for day, hours in trend.items():
        item = {'date' : day, 'data' : []}
        for hour, value in hours.items():
            item['data'].append({'hour' : hour + ':00', 'value' : value})
        response.append(item)

    return JsonResponse(data={'data': response}, safe=True)

def getBlankErrorInfo(request): 
    obj = BLANKSCREEN.objects.values_list('emptyPoints', 'timestamp')
    response = []
    for item in obj:
        timestamp = item[1]
        date = time.localtime(int(timestamp) / 1000)
        t = time.strftime('%Y-%m-%d %H:%M:%S', date)
        if int(item[0]) > 16:
            response.append( {'time': t , 'type': 'BlankError', 'message': '页面空点数为' + item[0] + '(> 16)'} )
    return JsonResponse(data={'data': list(reversed(response))}, safe=True)
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
                    'xhr' : 0,
                    'fetch' : 0
                }

        trend[day][hour]['xhr'] += 1 if item.status != '200-OK' else 0
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
                    'xhr' : 0,
                    'fetch' : 0
                }

        trend[day][hour]['fetch'] += 1 if item.success == 'False' else 0
    
    response = []
    for day, hours in trend.items():
        item = {'date' : day, 'data' : []}
        for hour, value in hours.items():
            item['data'].append({'hour' : hour + ':00', **value})
        response.append(item)
    return JsonResponse(data={'data': response}, safe=True)

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
                'xhr' : 0,
                'fetch' : 0
            }

        trend[format_date]['xhr'] += 1 if item.status != '200-OK' else 0
    #fetch trend
    for item in obj2.all():
        timestamp = item.timestamp
        date = time.localtime(int(timestamp) / 1000)
        format_date = time.strftime('%Y-%m-%d', date)
        if format_date not in trend:
            trend[format_date] = {
                'xhr' : 0,
                'fetch' : 0
            }
        trend[format_date]['fetch'] += 1 if item.success == 'False' else 0
    
    response = []
    for key, data in trend.items():
        for kind, value in data.items():
            response.append({'date': key, 'kind': kind, 'value': value})

    return JsonResponse(data={'data': response}, safe=True)

def getApiError(request):
    obj1 = xhr.objects
    obj2 = fetch.objects

    response_dict = {
        'data' : {
            'total' : len(obj1.all()) + len(obj2.all()),
            'xhr' : {
                'total' : len(obj1.all()),
                'error' : len(obj1.all()) - 
                          len(obj1.filter(status__exact='200-OK'))
            },
            'fetch' : {
               'total' : len(obj2.all()),
               'error' : len(obj2.filter(success__exact='false'))
            }
        }
    }
    return JsonResponse(data=response_dict, safe=True)

from django.forms.models import model_to_dict
def getApiErrorInfo(request):
    obj1 = xhr.objects.values_list('type', 'eventType', 'pathname', 'status', 'timestamp')
    obj2 = fetch.objects.values_list('type', 'method', 'url','status', 'timestamp')

    obj = list(merge(obj1, obj2))
    obj.sort(key=lambda x: int(x[-1]))
    response = []
    for item in obj:
        timestamp = item[4]
        date = time.localtime(int(timestamp) / 1000)
        t = time.strftime('%Y-%m-%d %H:%M:%S', date)
        if item[3] == '200-OK' or item[3] == '200':
            continue
        response.append( {'time': t, 'type' : item[0], 'eventType' : item[1], 'url' : item[2], 'status': item[3]})
    return JsonResponse(data={'data': list(reversed(response))}, safe=True)

def getApiInfo(request):
    obj1 = xhr.objects.all()
    obj2 = fetch.objects.all()

    obj = list(obj1) + list(obj2)
    response = []
    for item in obj:
        info = {'type' : item.type}
        info['method'] = item.method if item.type == 'fetch' else item.eventType
        info['url'] = item.url if item.type == 'fetch' else item.pathname
        body = model_to_dict(item)
        del body['id']
        info['body'] = body
        response.append(info)
    
    return JsonResponse(data={'data': list(reversed(response))}, safe=True)

def getApiErrorCharts(request):
    obj1 = xhr.objects
    obj2 = fetch.objects
    response_dict = {
        'data' : [
            {'type': 'xhr成功', 'value': len(obj1.filter(status__exact='200-OK'))},
            {'type': 'fetch成功', 'value': len(obj2.filter(success__exact='True'))},
            {'type': '失败', 'value': 
                len(obj2.filter(success__exact='False')) + len(obj1.all()) - len(obj1.filter(status__exact='200-OK'))}
        ]
    }
        
    return JsonResponse(data=response_dict, safe=True)

def getMean(value_list):
    return mean(list(map(lambda x: 0 if x[0] == '' else float(x[0]), value_list)))

#firstInput
def getFirstInputDelay(request):
    obj = firstInput.objects
    response_dict = {
        'data' : {
            "inputDelay": 0,
            "duration": 0,
            "startTime": 0,
        }
    }
    for key in response_dict['data'].keys():
        response_dict['data'][key] = getMean(obj.values_list(key))
    return JsonResponse(data=response_dict, safe=True)

#time
def getTiming(request):
    obj = timing.objects
    response_dict = {
        'data' : {
            "connectTime": 0,
            "ttfbTime": 0,
            "responseTime": 0,
            "parseDOMTime": 0,
            "domContentLoadedTime": 0,
            "timeToInteractive": 0,
            "loadTime": 0,
            "dnsTime": 0,
            "domReady": 0
        }
    }
    for key in response_dict['data'].keys():
        response_dict['data'][key] = getMean(obj.values_list(key))
    
    return JsonResponse(data=response_dict, safe=True)

#paint

def getPaint(request):
    obj = paint.objects
    response_dict = {
        'data' : 
            {
                'firstContentFulPaint' : getMean(obj.values_list('firstContentfulPaint')),
                'firstMeaningfulPaint' : getMean(obj.values_list('firstMeaningfulPaint')),
                'firstPaint' : getMean(obj.values_list('firstPaint')),
                'largestContentfulPaint' : getMean(obj.values_list('largestContentfulPaint'))
            } 
    }
    return JsonResponse(data=response_dict, safe=True)
#uv

def getUser(x):
    return x.uuid.split('&&')[0] + x.uuid.split('&&')[1]
def getUV(request):
    obj = set(map(getUser, list(pv.objects.all())))
    response_dict = {'data' : len(obj) }
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
        user[format_date].append(getUser(item))
    
    response = []
    for key in user.keys():
        response.append({'date': key , 'value': len(set(user[key]))})

    return JsonResponse(data={'data': response}, safe=True)

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
        user[day][hour].append(getUser(item))

    response = []
    for day, hours in user.items():
        item = {'date' : day, 'data' : []}
        for hour, value in hours.items():
            item['data'].append({'hour' : hour + ':00', 'value': len(set(value))})
        response.append(item)

    return JsonResponse(data={'data': response}, safe=True)

#pv
def getPV(request):
    obj = pv.objects.all()
    response_dict = {'data' : len(obj) }
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

    response = []
    for key, value in trend.items():
        response.append({'date': key, 'value': value})
    
    return JsonResponse(data={'data': response}, safe=True)

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

    response = []
    for day, hours in trend.items():
        item = {'date' : day, 'data' : []}
        for hour, value in hours.items():
            item['data'].append({'hour' : hour + ':00', 'value' : value})
        response.append(item)

    return JsonResponse(data={'data': response}, safe=True)

def getStaytime(request):
    obj = stayTime.objects.values_list('stayTime')
    all = list(map(lambda x: float(x[0]), obj))
    response_dict = {
        'data' : {
            'min' : min(all),
            'max' : max(all),
            'average' : mean(all), 
            'all' : all
        }
    }
    return JsonResponse(data=response_dict, safe=True)

def getStaytimeCharts(request):
    obj = stayTime.objects.values_list('stayTime')
    all = list(map(lambda x: float(x[0]), obj))
    response = [
        {'type': '<5s', 'value' : 0},
        {'type': '5s~60s', 'value' : 0},
        {'type': '1min~5min', 'value' : 0},
        {'type': '5min~15min', 'value' : 0},
        {'type': '>15min', 'value': 0},
    ]
    for item in all:
        item /= 1000
        if item < 5:
            response[0]['value'] += 1
        elif item < 60:
            response[1]['value'] += 1
        elif item / 60 < 5:
            response[2]['value'] += 1
        elif item /60 < 15:
            response[3]['value'] += 1
        else:
            response[4]['value'] += 1

    return JsonResponse(data={'data': response}, safe=True)