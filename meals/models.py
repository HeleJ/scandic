"""
meals models database
"""
from django.db import models
from django.utils.text import slugify
# Create your models here.


class Meals(models.Model):
    """
    Meals details for User
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preperation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        """
        Class Meta for verb
        """
        verbose_name = 'meal'
        verbose_name_plural = 'meals'
