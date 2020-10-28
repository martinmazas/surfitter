from django.forms import ModelForm
from .models import myUser
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput

class SignUpForm(ModelForm):
    password = forms.CharField(widget=PasswordInput(attrs={'type':'password'}))
    class Meta:
        model = myUser
        fields = ['fullname', 'email', 'user_name', 'password']

