from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
            'last_name': forms.TextInput(attrs={'class': 'form-control','required': True,'placeholder':'Your Last Name'}),
        }
    def clean_username(self):
        return self.cleaned_data['email']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': True, 'required': True, 'placeholder': 'Your Email Address'}))
    password = forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete':'current-password', 'required' : True,'placeholder':'Your Super Secret Password'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)
        self.fields['email'].label = _('Email')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data