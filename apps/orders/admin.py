<<<<<<< HEAD
"""
Admin configuration for the Orders app.
"""
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone', 'product', 'quantity', 'total_price', 'created_at')
    list_filter = ('created_at', 'product')
    search_fields = ('customer_name', 'phone', 'product__name')
    readonly_fields = ('created_at', 'total_price')
    ordering = ('-created_at',)
=======
"""
Admin configuration for the Orders app.
"""
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone', 'product', 'quantity', 'total_price', 'created_at')
    list_filter = ('created_at', 'product')
    search_fields = ('customer_name', 'phone', 'product__name')
    readonly_fields = ('created_at', 'total_price')
    ordering = ('-created_at',)
>>>>>>> 2dbe7600888bc565120e0649791a2e0c2e74f80c
