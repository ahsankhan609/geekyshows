from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from dj_auth.forms import *

# Deafult UserForm with Username and Password only. Not Firstname and Lastname
# def register(request): 
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request, 'Registration successful')            
#             return redirect('dj-login')
#     else:
#         fm = UserCreationForm()
#     context = {
#         'title': 'User Registration',
#         'form': fm
#     }
#     return render(request,'user_auth/register.html',context)

def register(request): # Own UserForm
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            # Let's say we want to add user to any specific group. Like Editor or Manager then first of all we create groups in the Admin pannle. Then we do the following
            # from django.contrib.auth.models import Group
            # user = fm.save()
            # group = Group.objects.get(name='Editor)
            # user.groups.add(group)
            messages.success(request, 'Registration successful.')            
            return redirect('dj-login')
    else:
        fm = SignUpForm()
    context = {
        'title': 'User Registration',
        'form': fm
    }
    return render(request,'user_auth/register.html',context)

def user_login(request):
    context = {
                'title': 'Login',
                'form': AuthenticationForm()
            }
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass) 
                if user is not None:
                    login(request, user)
                    return redirect('dj-dashboard')
        else:
            fm = AuthenticationForm()
        return render(request, 'user_auth/login.html',context)
    else:
        fm = AuthenticationForm()
    return redirect('dj-dashboard')

@login_required(login_url='dj-login')
def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request,'Profile updated successfully.')
                fm.save()
        else:
            if request.user.is_superuser == True: # Checdk whether user is superuser or not
                fm = EditAdminProfileForm(instance = request.user)
            else:
                fm = EditUserProfileForm(instance=request.user)
        context = {
            'title': 'Dashboard',
            'username': request.user.first_name + ' ' + request.user.last_name,
            'form': fm
        }
        #messages.success(request, 'Succesfully Logged In!')
        return render(request,'user_auth/dashboard.html',context)
    else:
        return redirect('dj-login')

def user_logout(request):
    request.session.flush() # flush session from database
    request.session.clear_expired() # clear expired session from browser
    logout(request)
    return redirect('dj-login')

# Change password with old password
@login_required(login_url='dj-login')
def change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user = request.user, data = request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user) # it will maintain the old session and did not logout user.
            messages.success(request, 'Your password was changed successfully!')
            return redirect('dj-dashboard')
    else:
        fm = PasswordChangeForm(user=request.user)
    context = {
        'title': 'Change Password',
        'form': fm
    }
    return render(request, 'user_auth/change_pass.html',context)

# Change password without old password
@login_required(login_url='dj-login')
def change_password1(request):
    if request.method == 'POST':
        fm = SetPasswordForm(user = request.user, data = request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user) # it will maintain the old session and did not logout user.
            messages.success(request, 'Your password was changed successfully!')
            return redirect('dj-dashboard')
    else:
        fm = SetPasswordForm(user=request.user)
    context = {
        'title': 'Change Password',
        'form': fm
    }
    return render(request, 'user_auth/change_pass1.html',context)
