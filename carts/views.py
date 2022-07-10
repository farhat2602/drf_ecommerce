from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from carts.models import Cart, CartItem, Coupon
from carts.serializers import CartSerializer, CouponSerializer
from products.models import Product


class CartItemCreate(APIView):

    def post(self, request):
        cart = Cart.objects.get(user=request.user, is_active=True)
        item = Product.objects.get(id=request.data['product_id'])
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=item,
            qty=1,
            total_price=item.price
        )
        if cart_item:
            cart_item.qty += 1
            cart_item.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_201_CREATED)


class CartItemDelete(APIView):

    def post(self, request, id):
        cart = Cart.objects.get(user=request.user, is_active=True)
        item = cart.cart_item.get(id=id)
        item.delete()
        cart.save()
        serializer = CartSerializer(cart, context={'request': request})
        return Response(serializer.data)


class CouponCreate(APIView):

    def post(self, request):
        serializer = CouponSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
