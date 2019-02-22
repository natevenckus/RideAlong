from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    #first_name = forms.CharField(max_length=30, required=True)
    #last_name = forms.CharField(max_length=30, required=True)
    #email = forms.EmailField(max_length=254, required=True, help_text='Enter valid edu email')

    class Meta:
        model = User
        fields = ('username','password1','password2')

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('FullName', 'SchoolEmail', 'ContactEmail', 'PhoneNum', 'Gender', 'DOB', 'SchoolName')