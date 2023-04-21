from django.urls import path
from enroll.views import *

urlpatterns = [
    path('student_info/',student_info, name='student_info'),
    path('student_detail/<int:stu_id>',student_detail, name='student_detail'),
    path('showformdata/',showformdata, name='showformdata'),
]