from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, EditProductForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector

def product_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = (
                Product.objects.annotate(
                    search = SearchVector('name', 'user'),
                ).filter(search=query)
            )

    return render(
        request,
        'products/search.html',
        {
            'form': form,
            'query': query,
            'results': results,
        }
    )


@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    
    return render(
        request,
        'products/index.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
        }
    )

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    
    return render(
        request,
        'products/product_detail.html',
        {
            'product': product
        }
    )

@login_required 
def create_product_view(request):
    if request.method == 'POST':
        form = ProductForm(data = request.POST, files = request.FILES, user = request.user)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
        
    else:
        form = ProductForm(user = request.user)
    context = {
        'form': form
    }

    return render(
        request,
        'products/create_product.html',
        context
    )

@login_required 
def edit_product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    if request.method == 'POST':
        product_form = EditProductForm(instance=product, data=request.POST, files = request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('products:product_detail', id=product.id, slug=product.slug)
    else:
        product_form = EditProductForm(instance=product)

    return render(
        request,
        'products/edit_product.html',
        {
            'product_form': product_form
        }
    )

@login_required
def delete_product(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    if request.method == 'POST':
        product.delete()
        
        return redirect('user_profile:profile', username=product.user.username)

    return render(
        request,
        'products/delete.html',
        {
            'product': product
        }
    )