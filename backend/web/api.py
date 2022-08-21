import json
from urllib import response
from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse, JsonResponse
from web.models import BLANKSCREEN
from web.models import resourceError,jsError,firstInput,timing,paint,xhr
from django.forms.models import model_to_dict

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
    row = paint.objects.last()
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

