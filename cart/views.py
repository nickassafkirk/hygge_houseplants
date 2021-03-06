from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product, Variant


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('add-to-cart-quantity'))
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
            if variant_id in list(cart[product_id]['product_variants'].keys()):
                # if variant exists increase it's quantity
                if int(cart[product_id]['product_variants'][variant_id]) + int(quantity) <= variant.quantity:
                    cart[product_id]['product_variants'][variant_id] += quantity
                    messages.success(
                        request, f'Updated {product.name} - {variant.name} quantity to {cart[product_id]["product_variants"][variant_id]}!'
                        )
                else:
                    messages.error(
                        request, 'Not enough stock, reduce quantity and try again!'
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
            if int(cart[product_id]) + quantity <= product.quantity:
                cart[product_id] += quantity
                messages.success(
                        request, f'Updated {product.name} quantity to {cart[product_id]}!'
                        )
            else:
                messages.error(
                        request, f'Not enough stock! ( {cart[product_id]} in cart, Max {product.quantity} available ) Reduce quantity and try again.'
                        )
        else:
            # else add it to cart dict and assign it's quantity value
            cart[product_id] = quantity
            messages.success(
                    request, f'{product.name} x {quantity} added to cart successfully!'
                    )

    # save the cart session cookie with updated values
    request.session['cart'] = cart

    # redirect to same product page
    return redirect('single_product', product_id=product.id)


def update_cart_qty(request, item_id):
    product_id = None
    variant_id = None

    if "-" in item_id:
        product_id = item_id.split('-')[0]
        variant_id = item_id.split('-')[1]
    else:
        product_id = item_id

    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity'))

    if variant_id:
        variant = get_object_or_404(Variant, pk=variant_id)
        if quantity > 0:
            if quantity <= variant.quantity:
                cart[product_id]['product_variants'][str(variant_id)] = int(quantity)
                messages.success(request, 'Quantity updated successfully')
            else:
                messages.error(
                        request, f'Not enough stock - {variant.quantity} available! Reduce quantity and try again.'
                        )
        else:
            del cart[product_id]['product_variants'][str(variant_id)]
            if not cart[product_id]['product_variants']:
                cart.pop(product_id)
            messages.success(
                request, 'Item removed from cart!')
    else:
        product = get_object_or_404(Product, pk=product_id)
        if quantity > 0:
            if quantity <= product.quantity:
                cart[product_id] = int(quantity)
                messages.success(request, 'Quantity updated successfully')
            else:
                messages.error(
                        request, f'Not enough stock! ( {cart[product_id]} in cart, Max {product.quantity} available ) Reduce quantity and try again.'
                        )
        else:
            cart.pop(product_id)
            messages.success(
                request, 'Item removed from cart!')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    try:
        product_id = None
        variant_id = None
        product = None
        variant = None

        if "-" in item_id:
            product_id = item_id.split('-')[0]
            variant_id = request.POST.get('variant')

        else:
            product_id = item_id

        product = get_object_or_404(Product, pk=product_id)

        cart = request.session.get('cart', {})

        if variant_id:
            variant = get_object_or_404(Variant, pk=variant_id)
            del cart[product_id]['product_variants'][str(variant_id)]
            if not cart[product_id]['product_variants']:
                cart.pop(product_id)
            messages.success(
                request, f'Item {product.name} - {variant.name} removed from cart!')
        else:
            cart.pop(product_id)
            messages.success(request, f'Item {product.name} removed from cart!')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
