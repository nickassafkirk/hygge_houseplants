from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


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
            categories = Category.objects.filter(nam__in=categories)

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

    template = 'products/single_product.html'

    context = {
        'product': product,
    }

    return render(request, template, context)

# Add new product view
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

# Edit Product View

# Delete Product View