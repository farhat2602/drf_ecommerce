from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from shops.models import Shop
from shops.serializers import ShopSerializer


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = (IsAdminUser, )

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


class ShopDetailView(APIView):

    def get_object(self, pk):
        try:
            Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def put(self, request, pk):
        shop = self.get_object(pk)
        serializer = ShopSerializer(shop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
