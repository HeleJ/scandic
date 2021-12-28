"""
meals app urls
"""
from django.urls import path
from . import views

APP_NAME = 'meals'

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('<slug:slug>', views.meal_detail, name='meal_detail')
]
