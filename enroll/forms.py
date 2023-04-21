from django.core import validators
from django import forms

# class StudentRegistration(forms.Form):
#     name = forms.CharField(label='Your Name', required=True,initial='',disabled=False,help_text='')
#     password = forms.CharField(label='Password',widget=forms.PasswordInput)
#     email = forms.EmailField()
#     address = forms.CharField(widget=forms.Textarea)
#     city = forms.CharField()
#     state = forms.CharField()
#     country = forms.CharField()

# This code is used for Form validation##########################################################################
class StudentRegForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
#     rpassword = forms.CharField(widget=forms.PasswordInput,label='Re-Enter Password')
    

# def clean(self):
#     cleaned_data = super(StudentRegistration, self).clean()
#     valpwd = self.cleaned_data['password']
#     valrpwd = self.cleaned_data['rpassword']
    
#     if valpwd != valrpwd:
#         raise forms.ValidationError('Invalid password')
# This code is used for Form validation##########################################################################