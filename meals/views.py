"""
meals app views.py
"""
from django.shortcuts import render

# Create your views here.
from .models import Meals


def meal_list(request):
    """
    for Meals page
    """
    meal_list = Meals.objects.all()

    context = {
        'meal_list': meal_list
    }

    return render(request, 'Meals/list.html', context)


def meal_detail(request, slug):
    """
    for Meal details page.
    """
    meal_detail = Meals.objects.get(slug=slug)

    context = {'meal_detail': meal_detail}

    return render(request, 'Meals/detail.html', context)
