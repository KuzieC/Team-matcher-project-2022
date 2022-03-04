from email.policy import default
from operator import mod
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 30, default = "name", unique= False)
    postcode = models.CharField(max_length = 7, default = "", unique = False)
    male = models.BooleanField(null = False, default = True)
    phone = models.CharField(max_length = 15, default = "", unique= False)
    age = models.IntegerField(null=False, default= 20)
    sport = models.CharField(max_length = 30, default = "", unique= False)
    experience = models.CharField(max_length = 30, default = "begginer", unique= False)
    username = models.CharField(max_length = 30, default = "", unique= True)
    password = models.CharField(max_length = 30, default = "", unique= False)
    #picture = models.ImageField()

class Search(models.Model):
    
    postcode = models.CharField(max_length = 7, default = "", unique = False)
    sport = models.CharField(max_length = 30, default = "", unique= False)
    mode = models.CharField(max_length = 30, default = "1v1", unique= False)