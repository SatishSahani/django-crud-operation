# from django.core import validators
from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            "username": forms.CharField(label='Mobile Number'),
            # "password": forms.CharField(label='Password', widget=forms.PasswordInput),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }

# class MobileLoginForm(AuthenticationForm):
#     username = forms.CharField(label='Mobile Number')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
