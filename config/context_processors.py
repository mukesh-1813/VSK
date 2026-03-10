"""
Context processors for shop-wide settings available in all templates.
"""
from django.conf import settings


def shop_settings(request):
    return {
        'SHOP_NAME': settings.SHOP_NAME,
        'SHOP_OWNER_PHONE': settings.SHOP_OWNER_PHONE,
    }
