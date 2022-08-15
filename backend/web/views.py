from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from . import models
# Create your views here.
def savedata(request):
    return HttpResponse("OK")