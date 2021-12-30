"""
aboutus models database
"""
from django.db import models

# Create your models here.


class AboutUs(models.Model):
    """
    User can see info(history) about_us
    """
    title = models.CharField(max_length=50)
    content = models.TextField()
    # image = models.ImageField(upload_to='about_us/')

    class Meta:
        """
        Class Meta for verb
        """
        verbose_name = 'about us'
        verbose_name_plural = 'about us'

    def __str__(self):
        return str(self.title)


class WhyChooseUs(models.Model):
    """
    User can see info sections about_us
    """
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        """
        Class Meta for verb
        """
        verbose_name = 'why choose us'
        verbose_name_plural = 'why choose us'

    def __str__(self):
        return str(self.title)
