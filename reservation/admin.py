"""
for Admin to see reservations
"""
from django.contrib import admin

# Register your models here.
from .models import Reservation


admin.site.register(Reservation)
