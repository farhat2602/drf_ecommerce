from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from products.models import Product


class Smartphone(Product):

    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.brand


class SmartphoneImage(models.Model):

    smartphone = models.ForeignKey(Smartphone, on_delete=models.CASCADE, related_name='smartphone_images')
    images = models.ImageField(upload_to='electronic/smartphone_images/')


class Laptop(Product):

    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_type


class LaptopImage(models.Model):

    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='laptop_images')
    images = models.ImageField(upload_to='electronic/laptop_images/')
