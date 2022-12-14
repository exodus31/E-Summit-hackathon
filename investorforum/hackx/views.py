import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout
from .models import Enterp, Investor

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
        i=1
        while True:
                if(Enterp.objects.filter(id=i)):
                        i=i+1
                else:
                        break
        ent_obj = Enterp.objects.create(id =i, username = username, email = email, name = name)
        ent_obj.save()
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
        i=1
        while True:
                if(Investor.objects.filter(id=i)):
                        i=i+1
                else:
                        break
        inv_obj = Investor.objects.create(id =i, username = username, email = email, name = name)
        inv_obj.save()
        return redirect('/')
    return render(request, 'signup_inv.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is None:
            messages.info(request, 'Invalid Credentials')
            return redirect('/login')                
        user_obj = Investor.objects.filter(username = username).first()
        if user_obj is None:
            user_obj2 = Enterp.objects.get(username = username)
            dj_login(request, user)
            if user_obj2.companyname == "":
                return redirect('/createprof/'+username)          
            else:
                return redirect('/')
        else:
            user_obj = Investor.objects.get(username = username)
            dj_login(request, user)
            if user_obj.details == "":
                return redirect('/createprof/' + username)
            else:
                return redirect('/')        
    return render(request, 'login.html')
       

def createprof(request, pk):
    if request.method == 'POST':                
        obj = Investor.objects.filter(username = pk).first()
        if obj is None:
            obj2 = Enterp.objects.get(username=pk)
            obj2.companyname = request.POST.get("companyname")
            obj2.onldesc = request.POST.get('onldesc')
            obj2.qpitch = request.POST.get('qpitch')
            obj2.cfunds = request.POST.get('cfunds')
            obj2.rfunding = request.POST.get('rfunding')
            obj2.field = request.POST.get('field')            
            obj2.save()
            return redirect('/')
        else:
            obj.details = request.POST.get("details")            
            obj.save()
            return redirect('/')
    return render(request, 'createprof.html')

def logoutuser(request):
    logout(request)
    messages.info(request, "Logged Out")
    return redirect('/')
