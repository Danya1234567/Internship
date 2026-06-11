from django.db import models as m

# Create your models here.

class Category(m.Model):
    name=m.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(m.Model):
    name=m.CharField(max_length=200)
    description=m.TextField()
    isAvaible=m.BooleanField(default=True)
    cost=m.DecimalField(max_digits=10, decimal_places=2)
    category=m.ForeignKey(Category,on_delete=m.DO_NOTHING)
    def __str__(self):
        return self.name

class Order(m.Model):
    name=m.CharField(max_length=200)
    car=m.ForeignKey('Cart',on_delete=m.DO_NOTHING, related_name='order')
    check_order=m.DecimalField(max_digits=10, decimal_places=2)
    created_at=m.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Cart(m.Model):
    created_at=m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    def total(self):
        return sum(item.calculate() for item in self.items.all())

class CartItem(m.Model):
    product=m.ForeignKey(Product,on_delete=m.DO_NOTHING)
    cart=m.ForeignKey(Cart,on_delete=m.DO_NOTHING, related_name='items')
    quantity=m.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} | {self.quantity}"

    def calculate(self):
        return  self.product.cost * self.quantity