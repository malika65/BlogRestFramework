from django.contrib import admin
from django.urls import path,include
from .views import registration,confirm,login,reset_password,new_password,edit_password

app_name = 'authe'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('confirm/<str:code>/',confirm,name = 'confirm'),
    path('login/',login,name = 'login'),
    path('reset/',reset_password,name = 'reset_password'),
    path('confirm/new_password/<str:code>/',new_password,name = 'new_password'),
    path('edit/password/',edit_password,name = 'edit_password'),



]
