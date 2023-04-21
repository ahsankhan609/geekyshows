from django.shortcuts import render
from enroll.models import Student
from enroll.models import StudentReg
from enroll.forms import StudentRegForm

def student_info(request):
    all_data = Student.objects.all()
    return render(request,'enroll/student_all.html',{'all_data':all_data})

def student_detail(request,stu_id):
    student_details = Student.objects.get(id=stu_id)
    return render(request,'enroll/student_detail.html',{'detail':student_details})

# def showformdata(request):
#     if request.method == 'POST':
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             name = fm.cleaned_data['name']
#             password = fm.cleaned_data['password']
#             email = fm.cleaned_data['email']
#             city = fm.cleaned_data['city']
#             state = fm.cleaned_data['state']
#             address = fm.cleaned_data['address']
#             country = fm.cleaned_data['country']
#             form_data = {
#                 'name': name,
#                 'password': password,
#                 'email': email,
#                 'city': city,
#                 'state': state,
#                 'address': address,
#                 'country': country
#             }
#             return render(request,'enroll/success.html',context=form_data)
#     else:
#         fm = StudentRegistration()
#     return render(request,'enroll/streg.html',{'form':fm})

# This code is used for Form validation##########################################################################
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            pwd = fm.cleaned_data['password']
            em = fm.cleaned_data['email']
            form_data = {
                'stu_name': nm,
                'stu_password': pwd,
                'stu_email': em,
            }
            reg = StudentReg(stu_name = nm, stu_password = pwd,stu_email=em)
            reg.save()
            return render(request,'enroll/success.html',context=form_data)
    else:
        fm = StudentRegForm()
    return render(request,'enroll/streg.html',{'form':fm})

# This code is used for Form validation##########################################################################