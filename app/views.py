
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Category, Product, Order, Cart, CartItem
from app.pagination import Pagination
from app.serializer import CategorySerializer, ProductSerializer, OrderSerializer, CartSerializer, CartItemSerializer
from user import serializer


class CategoryListView(APIView):
    def get(self, request):
        categories=Category.objects.all().order_by('id')
        paginator=Pagination()
        results=paginator.paginate_queryset(categories,request)
        serializer=CategorySerializer(results,many=True)
        return paginator.get_paginated_response(serializer.data)

class CategoryDetailView(APIView):
    serializer_class=CategorySerializer
    def get_object(self,pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request,pk):
        category=self.get_object(pk=pk)
        if not category:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CategorySerializer(category)
        return Response(serializer.data)

    def patch(self,request,pk):
        category=self.get_object(pk=pk)
        if not category:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CategorySerializer(category,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CategoryCreateView(APIView):
    serializer_class=CategorySerializer
    def post(self, request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CategoryDeleteView(APIView):
    serializer_class=CategorySerializer
    def delete(self,request,pk):
        try:
            category=Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListView(APIView):
    def get(self,request):
        product=Product.objects.all().order_by('id')
        paginator=Pagination()
        results=paginator.paginate_queryset(product,request)
        serializer=ProductSerializer(results,many=True)
        return paginator.get_paginated_response(serializer.data)

class ProductDetailView(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self,request,pk):
        product=self.get_object(pk=pk)
        if not product:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    def patch(self,request,pk):
        product=self.get_object(pk=pk)
        if not product:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductCreateView(APIView):

    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDeleteView(APIView):
    serializer_class=ProductSerializer
    def delete(self,request,pk):
        try:
            product=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderListView(APIView):
    def get(self,request):
        orders=Order.objects.all().order_by('id')
        paginator = Pagination()
        results = paginator.paginate_queryset(orders, request)
        serializer = CategorySerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)


class OrderCreateView(APIView):
    serializer_class = OrderSerializer
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    order_serializer = OrderSerializer
    def get_object(self,pk):
        try:
            return  Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def patch(self,request,pk):
        order=self.get_object(pk)
        if not order:
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=OrderSerializer(order,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OrderDeleteView(APIView):
    serializer_class = OrderSerializer
    def delete(self,request,pk):
        try:
            order=Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartListView(APIView):
    def get(self,request):
        cart=Cart.objects.all().order_by('id')
        paginator = Pagination()
        results = paginator.paginate_queryset(cart, request)
        serializer = CartSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

class CartCreateView(APIView):
    def post(self,request):
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CartDetailView(APIView):
    def get_object(self,pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return None
    def get(self,request,pk):
        cart=self.get_object(pk)
        if not cart:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CartSerializer(cart)
        return Response(serializer.data)

    def patch(self,request,pk):
        cart=self.get_object(pk)
        if not cart:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CartSerializer(cart,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CartDeleteView(APIView):
    serializer_class = CartSerializer
    def delete(self,request,pk):
        try:
            cart=Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartItemListView(APIView):
    def get(self,request):
        cartitem=CartItem.objects.all().order_by('id')
        paginator = Pagination()
        results = paginator.paginate_queryset(cartitem, request)
        serializer = CartItemSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

class CartItemDetailView(APIView):
    def get_object(self,pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return None

    def get(self,request,pk):
        cartitem=self.get_object(pk)
        if not cartitem:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CartItemSerializer(cartitem)
        return Response(serializer.data)


    def patch(self,request,pk):
        cartitem=self.get_object(pk)
        if not cartitem:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=CartItemSerializer(cartitem,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CartItemCreateView(APIView):
    serializer_class = CartItemSerializer
    def post(self,request):
        serializer=CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CartItemDeleteView(APIView):
    serializer_class = CartItemSerializer
    def delete(self,request,pk):
        try:
            cartitem=CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        cartitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)