from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description= models.TextField()
    price= models.FloatField(default=0)
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
