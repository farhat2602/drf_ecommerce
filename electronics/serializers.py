from rest_framework import serializers

from electronics.models import SmartphoneImage, Smartphone, LaptopImage, Laptop


class SmartphoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartphoneImage
        fields = '__all__'


class SmartphoneSerializer(serializers.ModelSerializer):
    images = SmartphoneImageSerializer(many=True, required=False)

    class Meta:
        model = Smartphone
        fields = '__all__'


class LaptopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopImage
        fields = '__all__'


class LaptopSerializer(serializers.ModelSerializer):
    images = LaptopImageSerializer(many=True, required=False)

    class Meta:
        model = Laptop
        fields = '__all__'
