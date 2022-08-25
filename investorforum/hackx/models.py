from operator import mod
from django.db import models

# Create your models here.

class Enterp(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Investor(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
