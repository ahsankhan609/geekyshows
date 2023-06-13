from django.shortcuts import render

def home(request):
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    context = {
        'count': newcount,
    }
    return render(request, 'pagecounter/home.html',context)
