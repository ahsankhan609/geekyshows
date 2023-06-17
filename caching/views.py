from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import *

@cache_page(60*15)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'caching/book_list.html', {
        'books': books
    })
