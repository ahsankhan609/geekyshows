from django.urls import path
from dj_messages.views import *

urlpatterns = [
    path('',home,name='dj-messages'),
]