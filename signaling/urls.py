from django.urls import path
from signaling.views import *

urlpatterns = [
    path('', home, name='signals')
]
