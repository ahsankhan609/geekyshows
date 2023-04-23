from django.urls import path
from dj_miniblog.views import *

urlpatterns = [
    path('', home ,name='dj-miniblog-home'),
    path('about/', about ,name='dj-miniblog-about'),
    path('contact/', contact ,name='dj-miniblog-contact'),
    path('dashboard/', dashboard ,name='dj-miniblog-dashboard'),
    path('register/', register ,name='dj-miniblog-register'),
    path('login_user/', login_user ,name='dj-miniblog-login-user'),
    path('logout_user/', logout_user ,name='dj-miniblog-logout-user'),
]