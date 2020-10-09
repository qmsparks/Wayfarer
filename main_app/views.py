from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Profile, City, Post
from .forms import Profile_Form, City_Form, Post_Form
# Create your views here.

# Base Views
def home(request):
    return render(request, 'home.html')



# show
def profile_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {'profile': profile}
    return render(request, 'profile/detail.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request,'post/detail.html', context)


# edit and update
def profile_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.method == 'POST':
        profile_form = Profile_Form(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_detail', profile_id=profile_id)
    else:
        profile_form = Profile_Form(instance=profile)
    context = {'profile': profile, 'profile_form': profile_form}
    return render(request, 'profile/edit.html', context)








