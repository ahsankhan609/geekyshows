from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# We are making this custom form becuae we want all fields for User Registration
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        labels = {'email':'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        label_suffix = ""
        label_attr = {'class': 'form-label'}

# We are using this class to update User Profile in the Dashboard
class EditUserProfileForm(UserChangeForm):
    # don't wan to show Password
    password = None
    class Meta:
        model = User
        # display the field's that user wants to Update
        fields = ('first_name', 'last_name')
        
# We are using this class to update Admin Profile in the Dashboard
class EditAdminProfileForm(UserChangeForm):
    # don't wan to show Password
    password = None
    class Meta:
        model = User
        # display the field's that user wants to Update
        fields = '__all__'