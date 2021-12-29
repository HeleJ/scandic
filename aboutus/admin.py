from django.contrib import admin

# Register your models here.

from .models import AboutUs 
from .models import WhyChooseUs


admin.site.register(AboutUs)
admin.site.register(WhyChooseUs)
