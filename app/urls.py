from django.urls import path

from app.views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryDeleteView, ProductListView, \
    ProductDetailView, ProductCreateView, ProductDeleteView, OrderListView, OrderDetailView, OrderCreateView, \
    OrderDeleteView, CartListView, CartDetailView, CartCreateView, CartDeleteView, CartItemListView, CartItemDetailView, \
    CartItemCreateView, CartItemDeleteView

urlpatterns = [
    # Categories
    path('categories/',CategoryListView.as_view(),name='category-list'),
    path('category/create/',CategoryCreateView.as_view(),name='category-create'),
    path('category/change/<int:pk>/',CategoryDetailView.as_view(),name='category-change'),
    path('category/delete/<int:pk>/',CategoryDeleteView.as_view(),name='category-delete'),
    path('category/<int:pk>/',CategoryDetailView.as_view(),name='category-detail'),

    # Products
    path('products/',ProductListView.as_view(),name='product-list'),
    path('product/create/',ProductCreateView.as_view(),name='product-create'),
    path('product/change/<int:pk>/',ProductDetailView.as_view(),name='product-change'),
    path('product/delete/<int:pk>/',ProductDeleteView.as_view(),name='product-delete'),
    path('product/<int:pk>/',ProductDetailView.as_view(),name='product-detail'),

    # Orders
    path('orders/',OrderListView.as_view(),name='order-list'),
    path('order/create/',OrderCreateView.as_view(),name='order-create'),
    path('order/change/<int:pk>/',OrderDetailView.as_view(),name='order-change'),
    path('order/delete/<int:pk>/',OrderDeleteView.as_view(),name='order-delete'),
    path('order/<int:pk>/',OrderDetailView.as_view(),name='order-detail'),

    # Carts
    path('carts/',CartListView.as_view(),name='cart-list'),
    path('cart/create/',CartCreateView.as_view(),name='cart-create'),
    path('cart/change/<int:pk>/',CartDetailView.as_view(),name='cart-change'),
    path('cart/delete/<int:pk>/',CartDeleteView.as_view(),name='cart-delete'),
    path('cart/<int:pk>/',CartDetailView.as_view(),name='cart-detail'),

    # CartItems
    path('cartitems/',CartItemListView.as_view(),name='cartitem-list'),
    path('cartitem/create/',CartItemCreateView.as_view(),name='cartitem-create'),
    path('cartitem/change/<int:pk>/',CartItemDetailView.as_view(),name='cartitem-change'),
    path('cartitem/delete/<int:pk>/',CartItemDeleteView.as_view(),name='cartitem-delete'),
    path('cartitem/<int:pk>/',CartItemDetailView.as_view(),name='cartitem-detail'),
]