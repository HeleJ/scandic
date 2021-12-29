from django.shortcuts import render
from .models import AboutUs, WhyChooseUs
# Create your views here.


def aboutus_list(request):
    about = AboutUs.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()

    context = {
        'about': about,
        'why_choose_us': why_choose_us,
    }

    return render(request, 'aboutus/about.html', context)
