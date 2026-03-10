"""
Views for the Orders app – handles order form and WhatsApp redirect.
"""
import re
import urllib.parse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views.decorators.http import require_http_methods
from apps.products.models import Product
from .models import Order


def order_form(request, product_id):
    """Show the order form for a specific product."""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'orders/order_form.html', {'product': product})


@require_http_methods(["POST"])
def create_order(request, product_id):
    """
    Validate & save the order, then redirect the customer to WhatsApp
    with a pre-filled message containing full order details.
    """
    product = get_object_or_404(Product, id=product_id)

    # ── 1. Extract & sanitise form data ──────────────────────────────────────
    customer_name = request.POST.get('customer_name', '').strip()
    phone         = request.POST.get('phone', '').strip()
    address       = request.POST.get('address', '').strip()
    pincode       = request.POST.get('pincode', '').strip()

    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity < 1:
            raise ValueError
    except (ValueError, TypeError):
        quantity = 1

    # ── 2. Server-side validation ─────────────────────────────────────────────
    errors = {}

    if not customer_name or len(customer_name) < 2:
        errors['customer_name'] = 'Please enter your full name.'

    if not re.match(r'^\+?[\d\s\-]{7,15}$', phone):
        errors['phone'] = 'Enter a valid phone number (7–15 digits).'

    if not address or len(address) < 5:
        errors['address'] = 'Please enter your delivery address.'

    if not re.match(r'^\d{4,10}$', pincode):
        errors['pincode'] = 'Enter a valid pincode.'

    if errors:
        return render(request, 'orders/order_form.html', {
            'product': product,
            'errors': errors,
            'form_data': {
                'customer_name': customer_name,
                'phone': phone,
                'address': address,
                'pincode': pincode,
                'quantity': quantity,
            },
        })

    # ── 3. Save order to database ─────────────────────────────────────────────
    order = Order.objects.create(
        product=product,
        customer_name=customer_name,
        phone=phone,
        address=address,
        pincode=pincode,
        quantity=quantity,
    )

    # ── 4. Build WhatsApp message ─────────────────────────────────────────────
    total = product.price * quantity

    message = (
        f"🛵 *NEW BIKE SPARE PART ORDER*\n"
        f"{'─' * 30}\n\n"
        f"📦 *Product Details*\n"
        f"  Name     : {product.name}\n"
        f"  Price    : ₹{product.price}\n"
        f"  Quantity : {quantity}\n"
        f"  Total    : ₹{total}\n\n"
        f"👤 *Customer Details*\n"
        f"  Name     : {customer_name}\n"
        f"  Phone    : {phone}\n"
        f"  Address  : {address}\n"
        f"  Pincode  : {pincode}\n\n"
        f"  Order ID : #{order.id}\n"
        f"{'─' * 30}\n"
        f"Please confirm availability & delivery. Thank you! 🙏"
    )

    encoded_message = urllib.parse.quote_plus(message)
    shop_phone = settings.SHOP_OWNER_PHONE
    whatsapp_url = f"https://wa.me/{shop_phone}?text={encoded_message}"

    # ── 5. Redirect to WhatsApp ───────────────────────────────────────────────
    # Pass order data to success page in session, then redirect
    request.session['order_success'] = {
        'order_id': order.id,
        'customer_name': customer_name,
        'product_name': product.name,
        'quantity': quantity,
        'total': str(total),
        'whatsapp_url': whatsapp_url,
    }

    return redirect('orders:success')


def order_success(request):
    """Show order confirmation and trigger WhatsApp redirect."""
    order_data = request.session.pop('order_success', None)
    if not order_data:
        return redirect('products:list')

    return render(request, 'orders/order_success.html', {'order': order_data})
