"""
about us app views.py
"""
from django.shortcuts import render
from .models import AboutUs, WhyChooseUs
# Create your views here.


def aboutus_list(request):
    """
    User can see info sections about_us
    """
    about = AboutUs.objects.last()
    why_choose_us = WhyChooseUs.objects.all()

    context = {
        'about': about,
        'why_choose_us': why_choose_us,
    }

    return render(request, 'aboutus/about.html', context)
