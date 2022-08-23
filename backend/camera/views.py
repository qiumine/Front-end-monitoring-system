import json
from urllib import response
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from web.views import savedata_resourceError,savedata_jsError,savedata_blank,savedata_xhr,savedata_firstInputDelay,savedata_timing,savedata_paint,savedata_pv,savedata_stayTime,savedata_fetch
# Create your views here.
def getdata(request):

    if request.method == 'POST':
        json_dict=json.loads(request.body)
        Type=json_dict.get('type')
        
        if Type == 'error':
            errorType=json_dict.get('errorType')
            if errorType == 'resourceError':
                return savedata_resourceError(request)
            elif errorType == 'jsError':
                return savedata_jsError(request)
            elif errorType == 'promiseError':
                return savedata_jsError(request)
            else:
                return HttpResponse("THIS ERROR DONT EXISTS")
        elif Type == 'blank':
            return savedata_blank(request)
        elif Type == 'xhr':
            return savedata_xhr(request)
        elif Type == 'firstInputDelay':
            return savedata_firstInputDelay(request)
        elif Type == 'timing':
            return savedata_timing(request)
        elif Type == 'paint':
            return savedata_paint(request)
        elif Type == 'fetch':
            return savedata_fetch(request)
        elif Type == 'stayTime':
            return savedata_stayTime(request)
        elif Type == 'pv':
            return savedata_pv(request)
        else:
            return HttpResponse("ERROR")
    else:
        return HttpResponse("GET")