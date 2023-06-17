from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from caching.views import *

urlpatterns = [
    path('',book_list, name='book_list'),
]
