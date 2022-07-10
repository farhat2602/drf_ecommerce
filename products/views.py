from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from eshop_config.permissions import IsOwnerOrReadOnly
from products.models import Product
from products.serializers import ProductPolymorphicSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductPolymorphicSerializer
    queryset = Product.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

    def retrieve(self, request, *args, **kwargs):
        post = self.get_object()
        post.view_count = post.view_count + 1
        post.save(update_fields=("view_count",))
        return super().retrieve(request, *args, **kwargs)
