from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('products/<product_id>', views.single_product, name='single_product'),
    path('add/', views.add_product, name='add_product'),
]
