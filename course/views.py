from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse('hello world from django. Home Page.')

def python(request):
    return HttpResponse('This is Python Course.')

def courses(request):
    course_detailes = {
        'name': 'Django',
        'price': 800,
        'description': 'Learn Django with full Web Development',
        'duration': 10,
        'dates' : datetime.now(),
    }
    return render(request, 'course/courses.html',context=course_detailes)

def html_detail(request):
    return render(request, 'course/html_detail.html')

def css_detail(request):
    return render(request, 'course/css_detail.html')