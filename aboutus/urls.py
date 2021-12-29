from django.urls import path
from . import views

APP_NAME = 'aboutus'

urlpatterns = [
    path('',views.aboutus_list, name='aboutus_list'),
]