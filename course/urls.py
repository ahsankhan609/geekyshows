from django.urls import path
from course.views import *

urlpatterns = [
    path('',home),
    path('python/',python),
    path('all/',courses),
    path('html_detail/',html_detail),
    path('css_detail/',css_detail,name='css_detail'),
    
    # Cookies URL
    path('set/',setcookie,name='set-cookie'),
    path('get/',getcookie,name='get-cookie'),
    path('del/',delcookie,name='del-cookie'),
    
    # Session URL
    path('set-sess/',setsession,name='set-session'),
    path('get-sess/',getsession,name='get-session'),
    path('del-sess/',delsession,name='del-session'),
]

