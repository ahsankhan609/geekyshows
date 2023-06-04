from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from dj_miniblog.views import *

urlpatterns = [
    path('', home ,name='dj-miniblog-home'),
    path('about/', about ,name='dj-miniblog-about'),
    path('contact/', contact ,name='dj-miniblog-contact'),
    path('dashboard/', dashboard ,name='dj-miniblog-dashboard'),
    path('register/', register ,name='dj-miniblog-register'),
    path('login_user/', LoginView.as_view(authentication_form=LoginForm, template_name='dj_miniblog/login_user.html') ,name='dj-miniblog-login-user'),
    path('logout_user/', logout_user ,name='dj-miniblog-logout-user'),
    path('add_post/', add_post ,name='dj-miniblog-add-post'),
    path('update_post/<int:id>/', update_post ,name='dj-miniblog-update-post'),
    path('delete_post/<int:id>/', delete_post ,name='dj-miniblog-delete-post'),
]