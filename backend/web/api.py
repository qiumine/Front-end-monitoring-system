import json
from urllib import response
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse, JsonResponse
from web.models import BLANKSCREEN
from web.models import resourceError,jsError,firstInput,timing,paint,xhr

def get_resourceError(request):
    response = json.dumps(list(resourceError.objects.all()))
    return JsonResponse(data=response)
def get_jsError(request):
    response = json.dumps(list(jsError.objects.all()))
    return JsonResponse(data=response)
def get_blank(request):
    response = json.dumps(list(BLANKSCREEN.objects.all()))
    return JsonResponse(data=response)
def get_xhr(request):
    response = json.dumps(list(xhr.objects().all()))
    return JsonResponse(data=response)
def get_firstInputDelay(request):
    response = json.dumps(list(firstInput.objects.all()))
    return JsonResponse(data=response)
def get_timing(request):
    response = json.dumps(list(timing.objects.all()))
    return JsonResponse(data=response)
def get_paint(request):
    response = json.dumps(list(paint.objects.all()))
    return JsonResponse(data=response)

