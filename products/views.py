from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all()

    template = 'products/products.html'

    context = {
        'products': products,
    }

    return render(request, template, context)
