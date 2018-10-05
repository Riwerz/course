from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Conspect
from taggit.managers import TaggableManager
from .subjects import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    name = forms.CharField(max_length=60, help_text='Required')
    surname = forms.CharField(max_length=60, help_text='Required')
        
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'surname', 'password1', 'password2')

class ConspectForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Заголовок', 'autocomplete': 'off'}))
    subject = forms.ChoiceField(choices = SUBJECT_CHOICES, widget=forms.Select())
    description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Краткое описание', 'autocomplete': 'off'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Текст'}))
    tags = TaggableManager()

    class Meta:
        model = Conspect
        fields = ('title', 'subject','description', 'text', 'tags')
