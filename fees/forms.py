from django.core import validators
from django import forms
from fees.models import Fee

class FeeRegForm(forms.ModelForm):
   class Meta:
       model = Fee
       fields = [
           'name',
           'email',
           'password',
       ]
       widgets = {
           'password': forms.PasswordInput
       }