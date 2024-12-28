from django.contrib import admin
from django.urls import path, include
from feedback import views  # Import your app's views

urlpatterns = [
     path('', views.home, name='home'), # Add a route for the root path
]
