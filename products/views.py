from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.forms import formset_factory
from django.db.models.functions import Lower
from .models import Product, Category, Variant
from .forms import ProductForm, VariantForm


# All products view
def products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    order = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category_name'
            if 'order' in request.GET:
                order = request.GET['order']
                if order == 'desc':
                    # if sort direction is ascending add - to sortkey to reverse sort order.
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                print('error blank search')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{order}'

    template = 'products/products.html'

    context = {
        'products': products,
        'search_criteria': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


# Single product view
def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {}

    if product.has_variants:
        variants = Variant.objects.filter(parent_product=product_id)
        context = {
            'product': product,
            'variants': variants,
        }
    else:
        context = {'product': product, }

    template = 'products/single_product.html'

    return render(request, template, context)


# Add new product view
def add_product(request):

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, prefix="product_form")
        if product_form.is_valid():
            new_product = product_form.save()
            has_variants = product_form['has_variants'].value()
            if has_variants:
                post_data = request.POST
                post_files = request.FILES
                print(post_files)
                print(new_product.id)
                variant_data = {
                    'parent_product': int(new_product.id),
                    'name': f'{new_product.name} {post_data["variant_form-color"]} {post_data["variant_form-size"]}',
                    'sku': post_data['variant_form-sku'],
                    'price':  post_data['variant_form-price'],
                    'color': post_data['variant_form-color'],
                    'size': post_data['variant_form-size'],
                    'quantity': post_data['variant_form-quantity'],
                    'image_url': post_data['variant_form-image_url'],
                }
                variant_form = VariantForm(variant_data, request.FILES)
                if variant_form.is_valid():
                    variant_form.save()
                    return redirect('single_product', product_id=new_product.id)
                else:
                    print('Form not valid', variant_form)
            else:
                # value is False if checkbox is not selected
                new_product = product_form.save()
                print(new_product.id)
                return redirect('single_product', product_id=new_product.id)
        else:
            print('invalid product form')
    else:

        product_form = ProductForm(prefix="product_form")
        variant_form = VariantForm(prefix="variant_form")
        variant_formset = formset_factory(VariantForm, extra=3)

        template = 'products/add_product.html'
        context = {
            'product_form': product_form,
            'variant_form': variant_form,
            'variant_formset': variant_formset,

        }

        return render(request, template, context)

# Edit Product View

# Delete Product View
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    return redirect(reverse('products'))
