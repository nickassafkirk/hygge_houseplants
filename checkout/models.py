import uuid
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

from products.models import Product, Variant


class Order(models.Model):
    order_number = models.CharField(max_length=25, null=False, editable=False)

    date = models.DateField(auto_now_add=True)

    full_name = models.CharField(max_length=50, null=False, blank=False)

    email = models.EmailField(max_length=250, null=False, blank=False)

    phone_number = models.CharField(max_length=20, null=True, blank=True)

    street_Address1 = models.CharField(max_length=80, null=False, blank=False)

    street_Address2 = models.CharField(max_length=80, null=True, blank=True)

    city_or_town = models.CharField(max_length=80, null=False, blank=False)

    state_or_province = models.CharField(
        max_length=80, null=False, blank=False)

    postcode = models.CharField(max_lenght=25, null=False, blank=False)

    country = CountryField(blank_label='Country *', null=False, blank=False)

    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)

    item_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='line_items')

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)

    variant = models.ForeignKey(
        Variant, blank=True, null=True, on_delete=models.CASCADE)

    quantity = models.IntegerField(
        max_length=3, blank=False, null=False, default=0)

    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)