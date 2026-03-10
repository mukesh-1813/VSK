<<<<<<< HEAD
"""
Admin configuration for the Products app.
"""
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'in_stock', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
=======
"""
Admin configuration for the Products app.
"""
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'in_stock', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
>>>>>>> 2dbe7600888bc565120e0649791a2e0c2e74f80c
