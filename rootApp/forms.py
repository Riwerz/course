from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    name = forms.CharField(max_length=60, help_text='Required')
    surname = forms.CharField(max_length=60, help_text='Required')
        
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'surname', 'password1', 'password2')