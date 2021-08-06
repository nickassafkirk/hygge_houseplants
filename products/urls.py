from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<product_id>', views.single_product, name='single_product'),
    path('add/', views.add_product, name='add_product'),
    path('add_variants/<product_id>', views.add_variants, name='add_variants'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
]
