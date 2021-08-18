from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages

from products.models import Product, Variant
from .models import Order, OrderLineItem
from .forms import OrderForm
from cart.contexts import shopping_cart
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        # payment intent id
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # update metadate section in stripe payment intent
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_details': request.POST.get('save_details'),
            'accept_marketing': request.POST.get('accept_marketing'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannont \
            be processed right now. Please try again.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'city_or_town': request.POST['city_or_town'],
            'county_or_state': request.POST['county_or_state'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)

        # Form is valid case
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            # If form is valid create and save each lineitem
            # This is reverse of building the cart_contents object
            for product_id, product_data in cart.items():
                try:
                    product = get_object_or_404(Product, pk=product_id)

                    # handle lineitem without variants
                    if isinstance(product_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            quantity=product_data,
                            product=product
                        )
                        order_line_item.save()

                    # handle lineitem with variant
                    else:
                        # iterate through product_data to extract variant_id & Qty
                        for variant_id, quantity in product_data["product_variants"].items():
                            variant = get_object_or_404(Variant, pk=variant_id)
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                variant=variant,
                                quantity=quantity,
                            )
                            order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        'One or more products, was not found - please contact us for assistance.')
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # save info to user's profile.
            print('Try clause success')
            request.session['save-details'] = 'save-details' in request.POST
            request.session['accept-marketing'] = 'accept-marketing' in request.POST
            return redirect(reverse('checkout_success', kwargs={"order_number": order.order_number, }))
        # Form is invalid - display message and return to request address
        else:
            messages.error(request, 'Checkout unsuccessful, check details and try again!')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, 'Your cart is empty!')
            return redirect(reverse('products'))

        current_order = shopping_cart(request)
        total = current_order['cart_total']
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'cart': cart,
            'form': form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Redirect to success page on successful cart checkout
    """

    save_details = request.session.get('save-details')
    order = get_object_or_404(Order, order_number=order_number)
    lineitems = OrderLineItem.objects.filter(order=order.id)
    messages.success(request, f'Order Confirmed! Your order number is: {order_number}.')
    if 'cart' in request.session:
        del request.session['cart']
    template = 'checkout/checkout_success.html'
    context = {
        'lineitems': lineitems,
        'order': order,
    }
    return render(request, template, context)
