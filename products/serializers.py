from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from electronics.models import Smartphone, Laptop
from electronics.serializers import SmartphoneSerializer, LaptopSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['view_count']


class ProductPolymorphicSerializer(PolymorphicSerializer):

    model_serializer_mapping = {
        Product: ProductSerializer,
        Smartphone: SmartphoneSerializer,
        Laptop: LaptopSerializer,
    }
