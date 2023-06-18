from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'ip': request.META.get('REMOTE_ADDR'),
    }
    return render(request, 'trackip/home.html',context)