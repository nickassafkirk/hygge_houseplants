from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def products(request):
    products = Product.objects.all()

    template = 'products/products.html'

    context = {
        'products': products,
    }

    return render(request, template, context)


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
