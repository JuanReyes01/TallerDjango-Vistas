from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.measurements_view, name='measurements_view'),
]
