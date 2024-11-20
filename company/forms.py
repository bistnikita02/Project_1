from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyProfile

class CompanyRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CompanyProfileForm(forms.ModelForm):
   
    class Meta:
        model = CompanyProfile
        fields = ['contact', 'company_name', 'address']

    