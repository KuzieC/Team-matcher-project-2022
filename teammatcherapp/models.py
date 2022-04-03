from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30, default = "", unique= False)
    city = models.CharField(max_length = 20, default = " ", unique = False)
    gender = models.CharField(max_length = 10, default = "", unique= False)
    phone = models.CharField(max_length = 15, default = "", unique= False)
    age = models.IntegerField(null=False, default=20)
    sport = models.CharField(max_length = 30, default = "", unique= False)
    experience = models.CharField(max_length = 30, default = "begginer", unique= False) 
    username = models.CharField(max_length = 30, default = "", unique= True)
    password = models.CharField(max_length = 30, default = "", unique= False)
    mode = models.CharField(max_length = 30, default = "", unique= False)
    def __str__(self):
        return self.name
    # #picture = models.ImageField()
   
class LeaderBoardPosition(models.Model):
    name = models.CharField(max_length = 30, default = "", unique= False)
    username = models.CharField(max_length = 30, default = "", unique= True)
    score = models.IntegerField(null=False, default = 0)
    def __str__(self):
        return self.name




# class Mode(models.Model):
#     title = models.CharField(max_length=10)
#     def __str__(self):
#         return self.title
# class Search(models.Model):
#     postcode = models.CharField(max_length = 7, default = "", unique = False)
#     sport = models.CharField(max_length = 30, default = "", unique= False)
#     mode = models.CharField(max_length = 30, default = "1v1", unique= False)
