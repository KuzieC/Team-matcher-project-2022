from django.db import models
from django.core.validators import RegexValidator


userValid = RegexValidator(
    r'^[0-9a-zA-Z\@.\+\-\_]*$', 'Username must contain letters, digits and @/./+/-/_ only')
phoneValid = RegexValidator(r'^[0-9]{10,15}$', 'Enter a valid phone number')
nameValid = RegexValidator(
    r'^[a-zA-Z\s]*$', 'Name must contain only letters and spaces')


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, default="",
                            unique=False, validators=[nameValid])
    city = models.CharField(max_length=20, default=" ", unique=False)
    gender = models.CharField(max_length=10, default="", unique=False)
    phone = models.CharField(max_length=15, default="",
                             unique=False, validators=[phoneValid])
    age = models.IntegerField(null=False, default=20)
    sport = models.CharField(max_length=30, default="", unique=False)
    experience = models.CharField(
        max_length=30, default="begginer", unique=False)
    username = models.CharField(
        max_length=30, default="", unique=True, validators=[userValid])
    password = models.CharField(max_length=30, default="", unique=False)
    mode = models.CharField(max_length=30, default="", unique=False)

    def __str__(self):
        return self.name
    # #picture = models.ImageField()


class LeaderBoardPosition(models.Model):
    name = models.CharField(max_length=30, default="", unique=False)
    username = models.CharField(max_length=30, default="", unique=True)
    score = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.name


class Items(models.Model):
    itemName = models.CharField(max_length=30, default="", unique=False)
    price = models.FloatField(null=False, default="", unique=False)
    description = models.CharField(max_length=60, default="", unique=False)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    foreignKey = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.itemName

# class Mode(models.Model):
#     title = models.CharField(max_length=10)
#     def __str__(self):
#         return self.title
# class Search(models.Model):
#     postcode = models.CharField(max_length = 7, default = "", unique = False)
#     sport = models.CharField(max_length = 30, default = "", unique= False)
#     mode = models.CharField(max_length = 30, default = "1v1", unique= False)
