from django.contrib import admin
from django.urls import path, include

from fruitApp.fruits import views

urlpatterns = [
    path('', views.index, name='')

]
