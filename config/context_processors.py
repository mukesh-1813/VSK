<<<<<<< HEAD
"""
Context processors for shop-wide settings available in all templates.
"""
from django.conf import settings


def shop_settings(request):
    return {
        'SHOP_NAME': settings.SHOP_NAME,
        'SHOP_OWNER_PHONE': settings.SHOP_OWNER_PHONE,
    }
=======
"""
Context processors for shop-wide settings available in all templates.
"""
from django.conf import settings


def shop_settings(request):
    return {
        'SHOP_NAME': settings.SHOP_NAME,
        'SHOP_OWNER_PHONE': settings.SHOP_OWNER_PHONE,
    }
>>>>>>> 2dbe7600888bc565120e0649791a2e0c2e74f80c
