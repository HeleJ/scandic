from django.urls import path
from . import views


APP_NAME = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
