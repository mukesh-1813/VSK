"""
Product model for VSK Bike Spare Parts shop.
"""
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Part Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (₹)")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Product Image")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock Quantity")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def in_stock(self):
        return self.stock > 0
