from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse

def senddata(request):
    return HttpResponse("OK")

