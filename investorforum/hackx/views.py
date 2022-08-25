from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup1.html')

def signup_ent(request):
    return render(request, 'signup_ent.html')

def signup_inv(request):
    return render(request, 'signup_inv.html')