from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Conspect
from taggit.managers import TaggableManager
from .subjects import *

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', label=gettext("Электронная почта"),
                             widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    name = forms.CharField(max_length=60, help_text='Required', label=gettext("Имя"),
                            widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    surname = forms.CharField(max_length=60, help_text='Required', label=gettext("Фамилия"),
                              widget=forms.TextInput(attrs={'autocomplete': 'off'}))
        
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'surname', 'password1', 'password2')

class ConspectForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': gettext('Заголовок'), 'autocomplete': 'off'}))
    subject = forms.ChoiceField(choices = SUBJECT_CHOICES, widget=forms.Select())
    description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': gettext('Краткое описание'), 'autocomplete': 'off'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': gettext('Текст')}))
    tags = TaggableManager()

    class Meta:
        model = Conspect
        fields = ('title', 'subject','description', "body", 'tags')
