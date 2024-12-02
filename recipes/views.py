from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Receta, Compra, Pago

# Create your views here.
def index(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Se ha ingresado correctamente")
                return HttpResponseRedirect("/home")
            else:
                messages.warning(request, "Usuario o contraseñas incorrectos")
    return render(request,"recipe/index.html",{"loginform":form})

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha registrado correctamente")
            return HttpResponseRedirect("") 
    return render(request,"recipe/register.html",{"registerform" : form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url="/")
def home(request):
    recipes = Receta.objects.all()
    context = {"recipe_list" : recipes}
    return render(request, "recipe/home.html", context)
