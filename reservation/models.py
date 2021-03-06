"""
reservation models database
"""
from django.db import models
# Create your models here.


class Reservation(models.Model):
    """
    Reservation details for User
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    Date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.name)
