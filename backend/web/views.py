import json
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from . import models
from web.models import BLANKSCREEN
from web.models import resourceError,jsError,firstInput,timing,paint,xhr,pv,stayTime,fetch
# Create your views here.
def savedata_resourceError(request):
    json_dict=json.loads(request.body)
    p=resourceError()
    names=resourceError._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_jsError(request):
    json_dict=json.loads(request.body)
    p=jsError()
    names=jsError._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_blank(request):
    print('once blank')
    json_dict=json.loads(request.body)
    p=BLANKSCREEN()
    names=BLANKSCREEN._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_xhr(request):
    json_dict=json.loads(request.body)
    p=xhr()
    names=xhr._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_firstInputDelay(request):
    json_dict=json.loads(request.body)
    p=firstInput()
    names=firstInput._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_timing(request):
    json_dict=json.loads(request.body)
    p=timing()
    names=timing._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_paint(request):
    json_dict=json.loads(request.body)
    p=paint()
    names=paint._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_pv(request):
    json_dict=json.loads(request.body)
    p=pv()
    names=pv._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_stayTime(request):
    json_dict=json.loads(request.body)
    p=stayTime()
    names=stayTime._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")
def savedata_fetch(request):
    json_dict=json.loads(request.body)
    p=fetch()
    names=fetch._meta.fields
    for i in range(len(names)):
        setattr(p,names[i].name,json_dict.get(names[i].name))
        print(names[i].name,':',json_dict.get(names[i].name))
    p.save()
    return HttpResponse("OK")