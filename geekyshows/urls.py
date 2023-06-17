"""geekyshows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
# from ecommerce.views import book_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('course/',include('course.urls')),
    path('enroll/',include('enroll.urls')),
    path('fees/',include('fees.urls')),
    path('dj_messages/',include('dj_messages.urls')),
    path('Auth/',include('dj_auth.urls')),
    path('miniblog/',include('dj_miniblog.urls')),
    path('counter/',include('pagecounter.urls')),
    path('books/',include('caching.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
