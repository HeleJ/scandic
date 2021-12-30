"""
home app views.py
"""
from django.shortcuts import render
from meals.models import Meals
from aboutus.models import WhyChooseUs
# Create your views here.


def home(request):
    """
    for home page
    """
    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    why_choose_us = WhyChooseUs.objects.all()

    context = {
        'meals': meals,
        'meal_list': meal_list,
        'why_choose_us': why_choose_us,
    }

    return render(request, 'home/index.html', context)
