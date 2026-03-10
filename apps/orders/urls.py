"""
URL configuration for the Orders app.
"""
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('<int:product_id>/', views.order_form, name='form'),
    path('<int:product_id>/create/', views.create_order, name='create'),
    path('success/', views.order_success, name='success'),
]
