from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Compra

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ["metodo_pago"]