from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout

# Create your views here.


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup1.html')

def signup_ent(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username = username).first():
            messages.info(request, 'Username Taken')
            return redirect('/signup_ent')    

        if User.objects.filter(email = email).first():
            messages.info(request, 'Email Already In Use')
            return redirect('/signup_ent')    

        user_obj=User(username = username, email=email)        
        user_obj.set_password(password)
        user_obj.save()
        return redirect('/')
    return render(request, 'signup_ent.html')

def signup_inv(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username = username).first():
            messages.info(request, 'Username Taken')
            return redirect('/signup_inv')    

        if User.objects.filter(email = email).first():
            messages.info(request, 'Email Already In Use')
            return redirect('/signup_inv')    

        user_obj=User(username = username, email=email)
        user_obj.is_staff=True
        user_obj.set_password(password)
        user_obj.save()
        return redirect('/')
    return render(request, 'signup_inv.html')

def logoutuser(request):
    logout(request)
    messages.info(request, "Logged Out")
    return redirect('/')