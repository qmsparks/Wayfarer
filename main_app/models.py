from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class City(models.Model):
    city_name = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class Profile(models.Model):
    name = models.CharField(max_length=20)
    current_city = models.CharField(max_length=50)
    date = models.DateField('joined on')
    #profile_Main_Img = models.ImageField(upload_to='images/') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    #date = models.DateField('created date')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Meta:
    ordering = ['date']