from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'title': 'Homepage',
        'posts': posts
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

@login_required(login_url='dj-miniblog-login-user')
def dashboard(request):
    posts = Post.objects.all()
    context = {
        'title': 'Dashboard',
        'posts': posts,
    }
    return render(request,'dj_miniblog/dashboard.html',context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! You become Author.')
            form.save()
    else:
        form = RegisterForm()
    context = {
        'title': 'Register - Become Author',
        'form': form,
    }
    return render(request,'dj_miniblog/register.html',context)

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return redirect(reverse('dj-miniblog-dashboard'))
        else:
            form = LoginForm()
        context = {
            'title': 'Login',
            'form': form,
        }
        return render(request, 'dj_miniblog/login_user.html', context)
    else:
        return redirect(reverse('dj-miniblog-dashboard'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/miniblog/')
