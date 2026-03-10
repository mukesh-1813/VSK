"""
Views for the Products app.
"""
from django.shortcuts import render
from .models import Product


def product_list(request):
    """Display all available products in the catalog."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
