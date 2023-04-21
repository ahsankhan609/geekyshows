from django.shortcuts import render
from fees.forms import FeeRegForm
from fees.models import Fee


def home(request):
    if request.method == 'POST':
        fm = FeeRegForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            pwd = fm.cleaned_data['password']
            em = fm.cleaned_data['email']
            reg = Fee(name=nm, password=pwd,email=em)
            reg.save()
        else:
            fm = FeeRegForm()
    else:
        fm = FeeRegForm()
    return render(request,'fees/fee.html',{'form':fm})