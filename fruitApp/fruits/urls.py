from django.contrib import admin
from django.urls import path, include

from fruitApp.fruits import views

urlpatterns = [
    path('', views.index, name=''),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.FruitFormView.as_view(), name='create-fruit'),
    path('fruties/<int:fruit_pk>/', include([
        path('details/', views.detail_fruit, name='detail-fruit'),
        path('edit/', views.edit_fruit, name='edit-fruit'),
        path('delete/', views.delete_fruit, name='delete-fruit'),
    ])),
]
