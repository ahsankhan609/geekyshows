from django.contrib import admin
from . models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','created_at','author']