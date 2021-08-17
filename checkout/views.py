from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your cart is empty!')
        return redirect(reverse('products'))
    else:
        form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'cart': cart,
            'form': form,
            'stripe_public_key': 'pk_test_51JFKHwHUYBtMekWnR6HNd1REv9M0rJPZxF0jPgZTK9zx6n94WotJ21upinfgsdm0VohzKg2Ww1hCKxsXGbwR9izm00aj8uBJTF',
            'client_secret': 'test',
        }
        return render(request, template, context)
