
from django.contrib import admin
from django.urls import path, include

from fruitApp.fruits import views

urlpatterns = [
    path('', include('fruitApp.fruits.urls')),
    path('admin/', admin.site.urls),

    path('categories/create/', views.create_category, name='create-category'),

]
