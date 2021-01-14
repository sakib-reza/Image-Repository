from typing import DefaultDict
from django.db import models

class ImageRepository(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, auto_now=False)
    user = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='images./')