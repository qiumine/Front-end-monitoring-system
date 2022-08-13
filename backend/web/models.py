from django.db import models

# Create your models here.
class BLANKSCREEN(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    emptypoints = models.IntegerField()
    screen = models.CharField(max_length=30)
    viewPoint = models.CharField(max_length=30)
    selector = models.CharField(max_length=100)

class resourceError(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    errortype = models.CharField(max_length=30)
    filename = models.CharField(max_length=100)
    tagname = models.CharField(max_length=100)
    selector = models.CharField(max_length=100)

class jsError(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    errortype = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    filename = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    stack = models.CharField(max_length=100)
    selector = models.CharField(max_length=100)

class firstInput(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    inputdelay = models.IntegerField()
    duration = models.IntegerField()
    starttime = models.IntegerField()
    selector = models.CharField(max_length=100)

class timing(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    connecttime = models.IntegerField()
    ttfbtime = models.IntegerField()
    responsetime = models.IntegerField()
    parsedomtime = models.IntegerField()
    domcontentloadedtime = models.IntegerField()
    timetointeractive = models.IntegerField()
    loadtime = models.IntegerField()

class paint(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    firstpaint = models.IntegerField()
    firstcontentfulpaint = models.IntegerField()
    firstmeaningfulpaint = models.IntegerField()
    largestcontentfulpaint = models.IntegerField()

class xhr(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    eventtype = models.CharField(max_length=30)
    pathname = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    duration = models.IntegerField()
    response = models.CharField(max_length=300)
    params = models.CharField(max_length=300)