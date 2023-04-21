from django.shortcuts import render

def home(request):
    return render(request, 'dj_messages/messages.html')
