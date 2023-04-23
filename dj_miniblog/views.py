from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *

def home(request):
    context = {
        'title': 'Homepage'
    }
    return render(request,'dj_miniblog/home.html',context)

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request,'dj_miniblog/about.html',context)

def contact(request):
    context = {
        'title': 'Contact Us'
    }
    return render(request,'dj_miniblog/contact.html',context)

def dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request,'dj_miniblog/dashboard.html',context)

def register(request):
    form = RegisterForm()
    context = {
        'title': 'Register',
        'form': form,
    }
    return render(request,'dj_miniblog/register.html',context)

def login_user(request):
    form = LoginForm()
    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request,'dj_miniblog/login_user.html',context)

def logout_user(request):
    return HttpResponseRedirect('/miniblog/')
