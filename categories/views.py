from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from categories.serializers import CategorySerializer, CategoryListSerializer


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryView(APIView):

    def get(self, request, slug):
        category = Category.objects.filter(slug=slug)
        serializer = CategoryListSerializer(category, many=True)
        return Response(serializer.data)
