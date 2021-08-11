from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name="calc_tax")
def calc_tax(total_price):
    tax_rate = settings.DEFAULT_TAX_RATE
    tax_rate = (1-tax_rate)
    return round((total_price * tax_rate), 2)


@register.filter(name="build_item_id")
def build_item_id(product_id, variant_id):
    item_id = f'{product_id}-{variant_id}'
    return item_id
