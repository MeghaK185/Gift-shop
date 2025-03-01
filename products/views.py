# products/views.py
from django.shortcuts import render, get_object_or_404,redirect
from .models import Product, Category

def home(request):
    products = Product.objects.filter(available=True)[:8]  # Show only 8 products on homepage
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'title': 'Welcome to Gift Shop'
    }
    return render(request, 'products/home.html', context)

def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
    
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)

def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Process immediate purchase
    # Redirect to checkout page
    return redirect('checkout')

def add_to_cart(request, product_id):
    # Your cart logic here
    # For example:
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')  # Or wherever you want to redirect after adding to cart