from django.db import models

# Create your models here.
class BLANKSCREEN(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    emptyPoints = models.CharField(max_length=30)
    screen = models.CharField(max_length=30)
    viewPoint = models.CharField(max_length=30)
    selector = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=30,default=0)

class resourceError(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    errorType = models.CharField(max_length=30)
    filename = models.CharField(max_length=100)
    tagName = models.CharField(max_length=100)
    selector = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=30,default=0)

class jsError(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    errorType = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    filename = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    stack = models.CharField(max_length=100)
    selector = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=30,default=0)

class firstInput(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    inputDelay = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    startTime = models.CharField(max_length=30)
    Selector = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=30,default=0)

class timing(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    connectTime = models.CharField(max_length=30)
    ttfbTime = models.CharField(max_length=30)
    responseTime = models.CharField(max_length=30)
    parseDOMTime = models.CharField(max_length=30)
    domContentLoadedTime = models.CharField(max_length=30)
    timeToInteractive = models.CharField(max_length=30)
    loadTime = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30,default=0)

class paint(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    firstPaint = models.CharField(max_length=30)
    firstContentfulPaint = models.CharField(max_length=30)
    firstMeaningfulPaint = models.CharField(max_length=30)
    largestContentfulPaint = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30,default=0)

class xhr(models.Model):
    kind = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    eventType = models.CharField(max_length=30)
    pathname = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    duration = models.CharField(max_length=30)
    response = models.CharField(max_length=300)
    params = models.CharField(max_length=300)
    timestamp = models.CharField(max_length=30,default=0)