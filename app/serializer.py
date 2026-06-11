from rest_framework import serializers

from app.models import Category, Product, Order, Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_category=serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model=Product
        fields=['id','name','description','isAvaible','cost','category','product_category']


class OrderSerializer(serializers.ModelSerializer):
    product_category = serializers.CharField(source='product.category', read_only=True)
    class Meta:
        model = Order
        fields=['id','name', 'car','check_order','created_at','product_category']
        read_only_fields=['created_at']


class CartItemSerializer(serializers.ModelSerializer):
    calculate=serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields=['id','product','cart','quantity','calculate']

    def get_calculate(self,obj):
        return obj.calculate()

class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)
    total=serializers.SerializerMethodField()
    class Meta:
        model=Cart
        fields=['id','items','total','created_at']
        read_only_fields=['created_at']

    def get_total(self,obj):
        return obj.total()