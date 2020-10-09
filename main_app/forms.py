from django.forms import ModelForm
from .models import City, Profile, Post

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'current_city']

class City_Form(ModelForm):
    class Meta:
        model = City
        fields = ['city_name', 'country_name']

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']
