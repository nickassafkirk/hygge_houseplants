from django.shortcuts import get_object_or_404

from products.models import Product


def shopping_cart(request):
    cart_contents = []
    total = 0
    product_count = 0
    bag = request.session.get('cart', {})

    for product_id, product_data in bag.items():
        # handle product without variant
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += product_data * product.price
            product_count += product_data
            cart_contents.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product
            })
        # handle product with variant
        else:
            product = get_object_or_404(Product, pk=product_id)
            # iterate through product_data to extract variant_id & Qty
            for key, value in product_data['product_variants'].items():
                total += value * product.price
                product_count = value
                cart_contents.append({
                    'product_id': product_id,
                    'quantity': value,
                    'product': product,
                    'variant': key,
                })

    # calculate shipping
    standard_shipping = 6.99
    free_shipping_over = 50

    if total < free_shipping_over:
        shipping = standard_shipping
        spend_for_free_shipping = free_shipping_over - total
    else:
        shipping = 0
        spend_for_free_shipping = 0

    # calculate total cart value
    cart_total = total + shipping

    # return context to be made available across site.
    context = {
        'cart_contents': cart_contents,
        'total': total,
        'product_count': product_count,
        'cart_total': cart_total,
        'shipping': shipping,
        'spend_for_free_shipping': spend_for_free_shipping,
    }

    return context
