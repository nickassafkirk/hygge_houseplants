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

    # get cart session variable or create if it doesn't exist

    # check if: product has variants
    # --check if a specific variant is in the cart
    # --if it is increase the quantity by quantity if not add it to cart

    # else: check if product is in the cart already
    # if it is increase the quantity by quantity if not add it to cart

    # save the cart session cookie with updated values

    # redirect to same page

    if 'variant-select' in request.POST:
        variant_id = request.POST['variant-select']
        variant = get_object_or_404(Variant, pk=variant_id)
        print(product, quantity, variant)
    else:
        print(product, quantity)
    return redirect('single_product', product_id=product.id)
