from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

# Base Views
def home(request):
    return render(request, 'home.html')

def profile_page(request):
    return render(request, 'profile/profile_page.html')

def post_detail(request):
    return render(request,'post/detail.html')