from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinLengthValidator

# Create your models here.




class City(models.Model):
    city_name = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    image_link = models.CharField(max_length=5000)

    def __str__(self):
        return self.city_name

class Profile(models.Model):
    name = models.CharField(max_length=20)
    current_city = models.CharField(max_length=50)
    date = models.DateField('joined on', default= datetime.now)
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name
  


class Post(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=250, validators=[MinLengthValidator(4)])
    date = models.DateField('created date', default= datetime.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



    class Meta:
        ordering = ['-date']