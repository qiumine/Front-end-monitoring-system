from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse

def getdata(request):
    if request.method == 'POST':
        content=request.POST.get('timestamp')
        return HttpResponse('POST CONTENT AT '+content)
    else:
        return HttpResponse("ERROR")

