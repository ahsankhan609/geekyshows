from django import forms
from dj_messages.models import *

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelName'
        fields = [
            'name',
            'email',
            'password',
        ]