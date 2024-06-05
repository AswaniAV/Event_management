from django.shortcuts import render,redirect
from .import views
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout 
# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already exists')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect('register')    
        elif password != confirmpassword:
            messages.error(request,'Password do not match')
            return redirect('register') 
        else:
            user = User.objects.create_user(username=username, email=email, password=password) 
            user.first_name = firstname
            user.last_name = lastname
            user.save() 
            messages.success(request,'Registration successful.. Please login.')  
            return redirect('login')  
    else:
     return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Replace 'home' with the name of your home page URL
        else:
            messages.error(request, "Invalid username or password")
            return render (request, 'login.html')
    else:
        return render (request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.info(request,'logout successfully..') 
    return redirect('login')

