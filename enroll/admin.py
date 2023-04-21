from django.contrib import admin
from enroll.models import Student
from enroll.models import StudentReg

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'address',
        'city',
        'state',
        'country',
        'enrolled_courses',
    )

class StudentRegAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'stu_name',
        'stu_email',
        'stu_password',
    )

admin.site.register(Student,StudentAdmin)
admin.site.register(StudentReg,StudentRegAdmin)