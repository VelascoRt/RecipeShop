from django.urls import path
from . import views

app_name = "recipes"
urlpatterns= [
    path("", views.index,name="index"),
    path("home/",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.detail, name="detail"),
    path("publicar/", views.create, name="create"),
]
