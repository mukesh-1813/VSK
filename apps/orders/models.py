"""
Order model for VSK Bike Spare Parts shop.
"""
from django.db import models
from apps.products.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', verbose_name="Product")
    customer_name = models.CharField(max_length=150, verbose_name="Customer Name")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    address = models.TextField(verbose_name="Delivery Address")
    pincode = models.CharField(max_length=10, verbose_name="Pincode")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} – {self.customer_name} ({self.product.name})"

    @property
    def total_price(self):
        return self.product.price * self.quantity
