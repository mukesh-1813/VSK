<<<<<<< HEAD
"""
Views for the Products app.
"""
from django.shortcuts import render
from .models import Product


def product_list(request):
    """Display all available products in the catalog."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
=======
"""
Views for the Products app.
"""
from django.shortcuts import render
from .models import Product


def product_list(request):
    """Display all available products in the catalog."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
>>>>>>> 2dbe7600888bc565120e0649791a2e0c2e74f80c
