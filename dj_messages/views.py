from django.shortcuts import render, redirect
from django.contrib import messages
from dj_messages.forms import * 

def home(request):
    if request.method == 'POST':
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            #messages.add_message(request,messages.SUCCESS,'User registration successful.')
            messages.success(request,'User registration successful.')
            return redirect('dj-messages')
    else:
        fm = StudentRegistrationForm()
    context = {
        'form': fm
    }        
    return render(request, 'dj_messages/messages.html',context)
