from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.forms import modelformset_factory
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
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            has_variants = product_form['has_variants'].value()
            print(has_variants)
            if has_variants:
                new_product = product_form.save()
                print(new_product.id)
                return redirect('add_variants', product_id=new_product.id)
            else:
                # value is False if checkbox is not selected
                new_product = product_form.save()
                return redirect('single_product', product_id=new_product.id)
        else:
            print('invalid product form')
            return redirect('add_product')
    else:
        product_form = ProductForm()
        template = 'products/add_product.html'
        context = {
            'product_form': product_form,
        }
        return render(request, template, context)


# Add variants
def add_variants(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    VariantFormSet = modelformset_factory(
        Variant,
        form=VariantForm,
        extra=1,
        )

    data = {
        'id': product.id,
        'name': product.name,
        'category': product.category,
        'sku': product.sku,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity,
        'image_url': product.image_url,
        'image': product.image,
        'has_variants': True,
        'available': product.available,
    }

    form = ProductForm(initial=data)

    if request.method == "POST":
        variant_formset = VariantFormSet(request.POST, request.FILES)

        if variant_formset.is_valid():
            for form in variant_formset:

                temp_form = form.save(commit=False)

                if temp_form.color:
                    color = temp_form.color
                else:
                    color = ""

                if temp_form.size:
                    size = temp_form.size
                else:
                    size = ""

                if not color and not size:
                    messages.error(request, "You must add a color or size")
                elif color and size:
                    name = f'{color} - {size}'.lower()
                elif color:
                    name = color.lower()
                elif size:
                    name = size.lower()

                temp_form.name = name
                temp_form.parent_product = product
                temp_form.save()
            return redirect('single_product', product_id=product_id)
        else:
            print('Form not valid', variant_formset)
            return redirect('add_product')
    else:
        variant_formset = VariantFormSet(queryset=Variant.objects.filter(parent_product=product.id))
        context = {
            'product': product,
            'product_form': form,
            'variant_formset': variant_formset,
        }
        template = 'products/add_variants.html'
        return render(request, template, context)


# Edit Product View
def edit_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            has_variants = product_form['has_variants'].value()
            if has_variants:
                new_product = product_form.save()
                return redirect('single_product', product_id=new_product.id)
            else:
                # value is False if checkbox is not selected
                new_product = product_form.save()
                return redirect('single_product', product_id=new_product.id)
        else:
            print('invalid product form')
            return redirect('add_product')
    else:
        product_form = ProductForm(instance=product)
        template = 'products/edit_product.html'
        context = {
            'product': product,
            'product_form': product_form,
        }
        return render(request, template, context)


# Delete Product View
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    return redirect(reverse('products'))
