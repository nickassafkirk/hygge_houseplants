from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from cart.contexts import shopping_cart
import stripe


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
