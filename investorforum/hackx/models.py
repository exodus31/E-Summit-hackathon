from operator import mod
from django.db import models

# Create your models here.

class Enterp(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100)
    onldesc = models.CharField(max_length=1000, default="Not Shared Yet")
    qpitch = models.CharField(max_length=1000, default="Not Shared Yet")
    cfunds = models.CharField(max_length=1000, default="Not Shared Yet")
    rfunding = models.CharField(max_length=1000, default="Not Shared Yet")
    field = models.CharField(max_length=1000, default="General")

    def __str__(self):
        return self.name

class Investor(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    details = models.CharField(max_length=500,default="")
    networth = models.CharField(max_length=1000, default="Not Shared Yet")
    comphold = models.CharField(max_length=1000, default="Not Shared Yet")
    invfield = models.CharField(max_length=1000, default="General")    

    def __str__(self):
        return self.name
