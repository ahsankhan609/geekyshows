from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=254,default='Not Available')
    city = models.CharField(max_length=254,default='Not Available')
    state = models.CharField(max_length=254,default='Not Available')
    country = models.CharField(max_length=254,default='Not Available')
    enrolled_courses = models.IntegerField(default=1)

class StudentReg(models.Model):
    stu_name = models.CharField(max_length=70)
    stu_email = models.EmailField(max_length=70)
    stu_password = models.CharField(max_length=64)    
