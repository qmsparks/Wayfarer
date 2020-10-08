from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Profile, City, Post
#Django Auth
from django.contrib import auth
#Django User Model
from django.contrib.auth.models import User
#Django decorate. Necessary for @login_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Home view
def home(request):
    return render(request, 'home.html')
#Register Form
def register(request):
    #from django-auth WC-SEI-817

    #Logic that handles data from request.method "POST"
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    #Checking and Compare password2 matches password1
        if password == password2:
            #check if username exists in db
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username already existed.'}
                return render(request, 'register.html', context) 
            else: #check email exists in DB
                if User.objects.filter(email=email_form).exists():
                    context = {'error': 'That email already exists.'}
                    return render(request, 'register.html', context)
                else: #if no duplicated usernme and email, store info in DB
                    user = User.objects.create_user(
                        username=username_form,
                        email=email_form,
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    # If registration is successful, following line will print
                    print('Registration is successful. Data is saved.')
                    return redirect('/') #return to homepage after registration
        else: #if passwords don't match
            context = {'error': 'Passwords do not match.'} 
            return render(request, 'home.html', context)
    else: #if there is nothing in the form
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username_form = request.POST['username']
        password_form = request.POST['password']
        # store user authenticate into user variable
        user = auth.authenticate(username=username_form, password=password_form)
        if user is not None:
            #Do login
            auth.login(request, user)
            #redirect back to profile page after successful login
            print('Login is successful!')
            return redirect('/')
        else:
            context = {'error': 'Wrong account credentials.'}
            messages.info(request, 'Message Info: Wrong account credentials')
            return render(request, 'home.html', context)
    else: 
        return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    #this tells where the log redirects
    return redirect('/')

@login_required
def profile_page(request, profile_id):

    profile = Profile.objects.get(id=profile_id)
    context = {'profile': profile}
    return render(request, 'profile/profile_page.html', context)

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request,'post/detail.html', context)

