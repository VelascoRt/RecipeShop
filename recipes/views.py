from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . forms import CreateUserForm, LoginForm, CompraForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Receta, Compra
from django.conf import settings
from cryptography.fernet import Fernet

f = Fernet(settings.ENCRYPT_KEY)

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
    if request.method == "POST":
        precio = request.POST.get("precio")
        premium = request.POST.get("es_premium")
        todas = request.POST.get("todas")
        if precio is not None:
            recipes = Receta.objects.filter(precio = precio)
        elif premium is not None:
            recipes = Receta.objects.filter(es_premium=premium)
        else:
            recipes = Receta.objects.all()
        context = {"recipe_list" : recipes}
        return render(request, "recipe/home.html", context)
    else:
        recipes = Receta.objects.all()
        context = {"recipe_list" : recipes}
    return render(request, "recipe/home.html", context)

@login_required(login_url="/")
def detail(request,pk):
    form = CompraForm(request.POST)
    if form.is_valid():
        form.instance.usuario_id = request.user
        form.instance.receta_id = Receta.objects.get(id=pk)
        form.instance.monto = Receta.objects.get(id=pk).precio
        compra_id = pk
        form.save()
        return HttpResponseRedirect("/home")
    else:
        form = CompraForm()
    recipe = get_object_or_404(Receta, pk = pk)
    return render(request,"recipe/detail.html",{"recipe":recipe, "compraform":form})
