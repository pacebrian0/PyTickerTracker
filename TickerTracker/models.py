from django.db import models
import datetime

class Price(models.Model):
    
    Date = models.FloatField()
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()
    Adj_Close = models.FloatField()
    Volume = models.FloatField()
    Name = models.CharField(max_length=10)

class Settings(models.Model):
    lastRun = models.DateField("DateLastRun", default=datetime.datetime(datetime.MINYEAR,1,1))
