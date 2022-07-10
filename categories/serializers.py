from rest_framework import serializers

from categories.models import Category
from products.serializers import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    product_category = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
