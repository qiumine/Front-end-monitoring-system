from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from web.views import savedata
# Create your views here.
def getdata(request):
    if request.method == 'POST':
        Type=request.POST.get('type')
        if Type == 'error':
            errorType=request.POST.get('errorType')
            if errorType == 'resourceError':
                return savedata(request)
            elif errorType == 'jsError':
                return savedata(request)
            elif errorType == 'promiseError':
                return savedata(request)
        elif Type == 'blank':
            return savedata(request)
        elif Type == 'xhr':
            return savedata(request)
        elif Type == 'firstInputDelay':
            return savedata(request)
        elif Type == 'timing':
            return savedata(request)
        elif Type == 'paint':
            return savedata(request)
        else:
            return HttpResponse("ERROR")
    else:
        return HttpResponse("ERROR")