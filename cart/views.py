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

    # get cart session variable or create empty dict if it doesn't exist
    cart = request.session.get('cart', {})

    # check if: product has variants
    if 'variant-select' in request.POST:
        variant_id = request.POST['variant-select']
        variant = get_object_or_404(Variant, pk=variant_id)

    if variant:
        # check if product is in the cart already
        if product_id in list(cart.keys()):
            # check if a specific variant is in the cart
            if variant in cart[product_id]['product_variants'].keys():
                # if variant exists increase it's quantity
                cart[product_id]['product_variants'][variant_id] += quantity
                messages.success(
                    request, f'Updated {product.name} - {variant.name} quantity to {cart[product_id]["product_variants"][variant_id]}!'
                    )
            else:
                # if not add prodcut variant to cart
                cart[product_id]['product_variants'][variant_id] = quantity
                messages.success(
                    request, f'{product.name} - {variant.name} x {quantity} added to cart successfully!'
                    )
        else:
            # create product and assign it's variants keys and values
            cart[product_id] = {'product_variants': {variant_id: quantity}}
            messages.success(
                    request, f'{product.name} - {variant.name} x {quantity} added to cart successfully!'
                    )
    else:
        # Handle product without variants
        if product_id in list(cart.keys()):
            # if product in cart, increase it's quantity value
            cart[product_id] += quantity
            messages.success(
                    request, f'Updated {product.name} quantity to {cart[product_id]}!'
                    )
        else:
            # else add it to cart dict and assign it's quantity value
            cart[product_id] = quantity
            messages.success(
                    request, f'{product.name} x {quantity} added to cart successfully!'
                    )

    # save the cart session cookie with updated values
    print(cart)
    request.session['cart'] = cart

    # redirect to same product page
    return redirect('single_product', product_id=product.id)
