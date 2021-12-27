"""
   contact app urls
"""
from django.urls import path
from . import views


APP_NAME = 'contact'

urlpatterns = [
    path('', views.send_email, name='send_email'),
    path('success/', views.send_success, name='send_success'),
]
