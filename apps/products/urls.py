<<<<<<< HEAD
"""
URL configuration for the Products app.
"""
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
]
=======
"""
URL configuration for the Products app.
"""
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
]
>>>>>>> 2dbe7600888bc565120e0649791a2e0c2e74f80c
