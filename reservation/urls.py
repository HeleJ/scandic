"""
   reservation app urls
"""
from django.urls import path
from . import views


APP_NAME = 'reservation'

urlpatterns = [
    path('', views.reserve_table, name='reserve_table'),
]
