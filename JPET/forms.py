from django.contrib.auth.forms import AuthenticationForm
from django.forms import *


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Login'}))
    password = CharField(widget=PasswordInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Password'}))

class SetupForm(Form):
    name = CharField(widget=TextInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Name'}))
    description = CharField(widget=Textarea(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Description'}))
    version = IntegerField(widget=NumberInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Version', 'min': '0'}))
    createDate = DateTimeField(widget=DateTimeInput(attrs={'class': 'mdl-textfield__input', 'placeholder': 'Create date'}))