from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

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
    # get the current user
    user = request.user
    # filter the posts by the user
    #posts = Post.objects.all()
    posts = Post.objects.filter(author=user)
    full_name = user.get_full_name()
    user_group_name = user.groups.all()
    context = {
        'title': 'Dashboard',
        'posts': posts,
        'fname': full_name,
        'groups': user_group_name,
    }
    return render(request,'dj_miniblog/dashboard.html',context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! You become an Author.')
            user = form.save()
            group = Group.objects.get(name='author-dj-miniblog')
            user.groups.add(group)
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
    
# Dashboard
# def dashboard (request):
#     if request.user.is_authenticated:
#         posts = Post.objects.all()
#         return render (request, 'dj_miniblog/dashboard.html', {'posts':posts})
#     else:
#         return HttpResponseRedirect('/login/')

@login_required(login_url='dj-miniblog-login-user')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/miniblog/')

# Add New Post
@login_required(login_url='dj-miniblog-login-user')
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['description']
                
                # get the current user
                user = request.user
                
                # create a pst object with the user as the author
                pst = Post(title=title, description=desc,author=user)
                pst.save()
                form = PostForm() # Flush the Form data
                # redirect to the dashboard
                return HttpResponseRedirect(reverse('dj-miniblog-dashboard'))
        else:
            form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'dj_miniblog/add_post.html',context)
    else:
        # use reverse to get the login url by its name 
        #return HttpResponseRedirect('/login/')
        return HttpResponseRedirect(reverse('login'))
    
# Update Post
@login_required(login_url='dj-miniblog-login-user')
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            
            # get the post object or show a 404 error page
            #pi = get_object_or_404(Post, pk=id)
            
            # get all data from the update form with the relevant id of the post
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                # redirect to the dashboard view
                return redirect(dashboard)
        else:
            # if submit is not clicked then we will only see the relevant(id)data
            pi = Post.objects.get(pk=id)
            
            #use this when the post does not exist and show a 404 error page instead of raising an exception
            #pi = get_object_or_404(Post, pk=id)
            
            form = PostForm(instance=pi)
        context = {
            'form': form,
        }    
        return render(request, 'dj_miniblog/update_post.html',context)
    else:
        return HttpResponseRedirect('/login/')

# Delete Post
@login_required(login_url='dj-miniblog-login-user')
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # use get_object_or_404 to get the Post object or raise a 404 error
            #pi = Post.objects.get(pk=id)
            pi = get_object_or_404(Post, pk=id)
            pi.delete()
        return redirect(dashboard)
    else: 
        return HttpResponseRedirect('/login/')

# Delete Post - Suggestion Provided by Bing-AI

# Based on web search results, here are some possible improvements for your code:

# You should use the @login_required decorator to protect your view from unauthorized access. This way, you don’t need to check if the user is authenticated inside the view function. You can also use the @user_passes_test decorator to check if the user is the owner of the post or has some other permission to delete it.

# You should use the get_object_or_404 shortcut to get the post object by its id. This will raise a 404 error if the post does not exist, instead of a 500 error that you would get with Post.objects.get.

# You should use the post argument in your url pattern and view function to match the post id. This will make your code more consistent and readable. You can also use a different name for your view function, such as post_delete, to avoid confusion with the delete method of the model.

# You should use the reverse function to generate the redirect url after deleting the post. This will make your code more robust and maintainable, as you don’t need to hardcode the url path. You can also use the success_url attribute of the DeleteView class-based view to simplify your code further.

# Here is an example of how your code could look like after applying these suggestions:
    
# @login_required
# @user_passes_test(lambda u: u.is_superuser) # or some other condition
# def post_delete(request, post):
#     if request.method == 'POST':
#         pi = get_object_or_404(Post, pk=post)
#         pi.delete()
#         return redirect(reverse('dashboard'))
#     else:
#         return redirect(reverse('login')) 
