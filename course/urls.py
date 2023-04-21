from django.urls import path
from course.views import *

urlpatterns = [
    path('',home),
    path('python',python),
    path('all/',courses),
    path('html_detail/',html_detail),
    path('css_detail/',css_detail,name='css_detail'),
]

