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

    # calculate total cart value
    # calculate shipping

    # return context to be made available across site.

