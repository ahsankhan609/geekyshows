from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control','required': True,'placeholder':'Your Secret Password'}))
    password2 = forms.CharField(label='Re-Type Password',widget=forms.PasswordInput(attrs={'class': 'form-control','required': True,'placeholder':'Your Secret Password Again'}))
    class Meta:
        model = User
        fields = ('email','first_name','last_name')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','required': True,'placeholder':'Your Email Address'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','required': True,'placeholder':'Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','required': True,'placeholder':'Your Last Name'})
        }
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.EmailInput(attrs={'class': 'form-control','autofocus':True, 'required' : True,'placeholder':'Your Email Address'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete':'current-password', 'required' : True,'placeholder':'Your Super Secret Password'}))