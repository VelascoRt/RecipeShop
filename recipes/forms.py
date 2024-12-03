from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import PasswordInput, TextInput
from .models import Compra, Receta

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

DIFICULTAD = [
    ('FACIL', 'Fácil'),
    ('MEDIA', 'Media'),
    ('DIFICIL', 'Díficil'),
]



class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        es_premium = forms.BooleanField()
        precio = forms.DecimalField()
        dificultad = forms.ChoiceField(choices=DIFICULTAD)
        fields = ["titulo","descripcion","categoria","dificultad","tiempo_preparacion","precio","imagen_url","es_premium"]
        widgets={
            'titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria' : forms.TextInput(attrs={'class':'form-control'}),
            'tiempo_preparacion' : forms.NumberInput(attrs={'class':'form-control'}),
            'precio' : forms.NumberInput(attrs={'class':'form-control'}),
            'imagen_url' : forms.TextInput(attrs={'class':'form-control'}),

        }