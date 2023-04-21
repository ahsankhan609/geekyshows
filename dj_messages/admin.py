from django.contrib import admin
from dj_messages.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'email', 'password'
    ]