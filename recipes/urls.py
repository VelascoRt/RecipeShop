from django.urls import path
from . import views

app_name = "recipes"
urlpatterns= [
    path("", views.index,name="index"),
    path("home/",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("logout/", views.logout, name="logout"),
]
