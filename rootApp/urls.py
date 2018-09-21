from django.urls import path
from . import views

urlpatterns = [
    path('', views.load_mainpage),
    path('login', views.load_login)
]