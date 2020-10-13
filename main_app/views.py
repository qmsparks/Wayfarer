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
from .forms import Profile_Form, City_Form, Post_Form
import copy
# Create your views here.
# Home view
def home(request):
    return render(request, 'home.html')

#Register Form
def register(request):
    #from django-auth WC-SEI-817
    error_message = ''
    
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
                error_message = 'Username already existed.'
                context = {'error': error_message}
                return render(request, "home.html", context)
            else: #check email exists in DB
                if User.objects.filter(email=email_form).exists():
                    context = {'error': 'That email already exists.'}
                    return HttpResponse("Email already Exists")
                else: #if no duplicated usernme and email, store info in DB
                    user = User.objects.create_user(
                        username=username_form,
                        email=email_form,
                        password=password,
                        first_name=first_name,
                        last_name=last_name
                    )
                    user.save()

                    profile = Profile(
                        name = f"{user.first_name} {user.last_name}",
                        user = user,
                        current_city = request.POST["current_city"],
                    )
                    profile.save()
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
            return redirect('profile_detail', user.id)
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
  
# show
@login_required
def profile_detail(request, profile_id):
    user = User.objects.get(id=profile_id)
    context = {'user': user}
    return render(request, 'profile/detail.html', context)


@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request,'post/detail.html', context)

@login_required
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user.id == post.profile.user_id:
        if request.method == 'POST':
            post_form = Post_Form(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect('post_detail', post_id=post_id)
        else:
            post_form = Post_Form(instance=post)
        context = {'post': post, 'post_form': post_form}
        return render(request, 'post/edit.html', context)
    else:
        return HttpResponse("You are not Authorized to edit this post")

# delete
@login_required
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user.id == post.profile.user_id:
        post = Post.objects.get(id=post_id)
        city = post.city_id
        Post.objects.get(id=post_id).delete()
        return redirect('city_detail', city_id = city)
    else:
        return HttpResponse("You are not Authorized to delete this post")


# edit and update
@login_required
def profile_edit(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.user.id == profile.user_id:
        if request.method == 'POST':
            profile_form = Profile_Form(request.POST, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile_detail', profile_id=profile.user.id)
        else:
            profile_form = Profile_Form(instance=profile)
        context = {'profile': profile, 'profile_form': profile_form}
        return render(request, 'profile/edit.html', context)
    else:
        return redirect('home')


#SECTION City
def city_detail(request, city_id):
    city = City.objects.get(id =city_id)
    cities = City.objects.all();
    post_form = Post_Form()
    context = {
        'city': city,
        'post_form': post_form,
        'cities': cities,
    }
    return render(request, 'city/detail.html', context)

@login_required
def city_edit(request, city_id):
    city = City.objects.get(id=city_id)
    if request.method == 'POST':
        city_form = City_Form(request.POST, instance=city)
        if city_form.is_valid():
            city_form.save()
            return redirect('city_detail', city_id=city.user.id)
    else:
        city_form = City_Form(instance=city)
    context = {'city': city, 'city_form': city_form}
    return render(request, 'city/edit.html', context)

@login_required
def add_post(request, city_id):
    city = City.objects.get(id=city_id)
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            user_id = request.user.id
            profile = Profile.objects.get(user=user_id)
            new_post = Post(
                title = request.POST['title'],
                author = request.POST['author'],
                content = request.POST['content'],
                city = city,
                profile = profile
            )
            new_post.save()
            return redirect('city_detail', city_id=city_id)
        else:
            context = {'formInvalid': 'Form not properly filled out please try again.'}
            return render(request, 'city/detail.html', context)