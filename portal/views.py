from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile,Job
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
             my_user = User.objects.create_user(uname, email, pass1)
             my_user.save()
        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
                return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')


def logout(request):
    return redirect('login')


def profile(request):
    if request.method == 'POST':
                first_name = request.POST.get('first_name', '')
                last_name = request.POST.get('last_name', '')
                biography = request.POST.get('biography', '')
                email = request.POST.get('email', '')
                phone = request.POST.get('phone', '')
                address = request.POST.get('address', '')
                city = request.POST.get('city', '')
                state = request.POST.get('state', '')
                country = request.POST.get('country', '')
                zipcode = request.POST.get('zipcode', '')
                profile = Profile(first_name=first_name, last_name=last_name, biography=biography, email=email,
                                  phone=phone, address=address, city=city, state=state, country=country, zipcode=zipcode)
                profile.save()
    return render(request, 'profile.html')


def job(request):
            if request.method == 'POST':
                title = request.POST.get('title', '')
                job_type = request.POST.get('job_type', '')
                description= request.POST.get('description', '')
                location = request.POST.get('lacation', '')
                company = request.POST.get('company', '')
                job = Job(title=title,job_type=job_type,description=description,location=location,company=company)
                job.save()
            return render ( request, 'job.html')

def about(request):
    return render ( request, 'about.html')
