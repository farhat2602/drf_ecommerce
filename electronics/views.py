from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from electronics.models import Smartphone, Laptop
from electronics.serializers import SmartphoneSerializer, LaptopSerializer
from shops.models import Shop


class SmartphoneListView(generics.ListAPIView):

    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer


class SmartphoneCreateView(APIView):

    def post(self, request):
        user = request.user
        shop = Shop.objects.filter(owner=user.id)
        if shop:
            serializer = SmartphoneSerializer(shop)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LaptopListView(generics.ListAPIView):

    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class LaptopCreateView(generics.CreateAPIView):
    serializer_class = LaptopSerializer

    def create(self, request, *args, **kwargs):
        owner = request.data['owner']
        if owner.is_shop_owner:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
