from django.shortcuts import render, redirect, reverse, get_object_or_404
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

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('products'))
        else:
            print('invalid form')
    else:
        form = ProductForm()
        template = 'products/add_product.html'
        context = {
            'form': form,
        }

        return render(request, template, context)


def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    template = 'products/single_product.html'

    context = {
        'product': product,
    }

    return render(request, template, context)
