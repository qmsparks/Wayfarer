from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Profile

# Create your views here.

# Base Views
def home(request):
    return render(request, 'home.html')

def profile_page(request):
    profile = Profile.objects.get(id = profile_id)
    context = {'profile': profile}
    return render(request, 'profile/profile_page.html', context)

def post_detail(request):
    post = Post.objects.get(id = post_id)
    context = {'post': post}
    return render(request,'post/detail.html', context)