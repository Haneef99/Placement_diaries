from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class loginForm(forms.ModelForm):
    model = User
    fields = ['username','password']


class UserCreation(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username' , 'email', 'password1', 'password2']