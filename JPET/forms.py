from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Login'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))