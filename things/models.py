from django.db import models
from django.core.validators import MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length =30,unique = True, blank = False)
    description = models.TextField(blank = True, max_length=120)
    quantity = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(100)])
