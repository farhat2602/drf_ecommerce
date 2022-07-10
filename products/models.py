from django.core.validators import MaxValueValidator
from django.db import models

from categories.models import Category
from shops.models import Shop
from polymorphic.models import PolymorphicModel


class Product(PolymorphicModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
