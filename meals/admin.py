from django.contrib import admin

# Register your models here.

from django_summernote.admin import SummernoteModelAdmin

from .models import Meals


class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name', 'preperation_time', 'people', 'price']
    search_fields = ['name', 'description']
    list_filter = ('people')


admin.site.register(Meals)
