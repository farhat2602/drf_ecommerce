from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='media/shop_images/')
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
