from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, Variant


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    print(request.POST)
    product = get_object_or_404(Product, pk=product_id)
    quantity = request.POST.get('add-to-cart-quantity')
    variant = None

    if 'variant-select' in request.POST:
        variant_id = request.POST['variant-select']
        variant = get_object_or_404(Variant, pk=variant_id)
        print(product, quantity, variant)
    else:
        print(product, quantity)
    return redirect('single_product', product_id=product.id)
