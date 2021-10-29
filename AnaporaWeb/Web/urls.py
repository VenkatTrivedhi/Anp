from django.contrib import admin
from django.urls import path
from .views import Txt_handler

urlpatterns = [
    path('',Txt_handler,name=''),
]