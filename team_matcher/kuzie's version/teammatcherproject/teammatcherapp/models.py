from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30, default = "name", unique= False)
    postcode = models.CharField(max_length = 10, default = "", unique = False)
    gender = models.CharField(max_length = 1, default = "M", unique= False)
    phone = models.CharField(max_length = 15, default = "", unique= False)
    age = models.IntegerField(null=False, default= 20)
    sport = models.CharField(max_length = 30, default = "", unique= False)
    experience = models.CharField(max_length = 30, default = "begginer", unique= False) 
    username = models.CharField(max_length = 30, default = "", unique= False)
    password = models.CharField(max_length = 30, default = "", unique= False)
    mode = models.CharField(max_length = 30, default = "", unique= False)
    # #picture = models.ImageField()
   

# class Mode(models.Model):
#     title = models.CharField(max_length=10)
#     def __str__(self):
#         return self.title
# class Search(models.Model):
#     postcode = models.CharField(max_length = 7, default = "", unique = False)
#     sport = models.CharField(max_length = 30, default = "", unique= False)
#     mode = models.CharField(max_length = 30, default = "1v1", unique= False)