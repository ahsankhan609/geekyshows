from django.urls import path
from dj_miniblog.views import *

urlpatterns = [
    path('', register ,name='dj-reg'),
    path('login/', user_login ,name='dj-login'),
    path('dashboard/', dashboard ,name='dj-dashboard'),
    path('logout/', user_logout ,name='dj-logout'),
    path('change_password/', change_password ,name='dj-ch-password'),
    path('change_password1/', change_password1 ,name='dj-ch-password1'),
]