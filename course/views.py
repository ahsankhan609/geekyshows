from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

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

# set cookie
def setcookie(request):
    response = render(request, 'course/setcookie.html')
    #response.set_cookie('name','ABC', max_age=86400) # this max age denominate number of seconds
    #response.set_cookie('name','ABC', expires=datetime.utcnow() + timedelta(days=2)) # this expires in 2 days
    response.set_signed_cookie('name','ABC', salt = 'nm',expires=datetime.utcnow() + timedelta(days=2)) # this will set the signed cookie with salt
    return response

# get cookie
def getcookie(request):
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name','XYZ') # If we want to set the default value,when cookie is not set
    name = request.get_signed_cookie('name',salt='nm',default='XYZ') # we set default value to ignore the wrong SALT error
    context = {
        'name': name,
    }
    return render(request, 'course/getcookie.html', context)

# del cookie
def delcookie(request):
    response = render(request, 'course/delcookie.html')
    response.delete_cookie('name')
    return response

############################################################################################################

# set session
import random
def setsession(request):
    request.session['name'] = random.randint(0,5)
    
    # Now set the Test cookie to see whether client browser can support cookies
    request.session.set_test_cookie()
    return render(request, 'course/setsession.html')

# get session
def getsession(request):
    #name = request.session['name']
    name = request.session.get('name', default='No Session')
    keys = request.session.keys()
    items = request.session.items()
    #age = request.session.setdefault('age', '26') # it will set and get the session with default value.
    context = {
        'name': name,
        'keys': keys,
        'items': items,
        #'age': age,
    }
    return render(request, 'course/getsession.html',context)

# delete session
def delsession(request):
    request.session.delete_test_cookie() # delete test cookie
    request.session.flush() # flush session from database
    request.session.clear_expired() # clear expired session from browser
    return render(request, 'course/delsession.html')