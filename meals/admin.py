"""
for superUser
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Meals
# Register your models here.


class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    # instead of ModelAdmin
    """
    for superuser to work with
    """
    summernote_fields = '__all__'
    list_display = ['name', 'preperation_time', 'people', 'price']
    search_fields = ['name', 'description']
    list_filter = ('people', 'price')


admin.site.register(Meals, MealsAdmin)
