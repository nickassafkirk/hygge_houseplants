import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from products.models import Product, Variant


class Order(models.Model):
    order_number = models.CharField(max_length=25, null=False, editable=False, unique=True)

    date = models.DateField(auto_now_add=True)

    full_name = models.CharField(max_length=50, null=False, blank=False)

    email = models.EmailField(max_length=250, null=False, blank=False)

    phone_number = models.CharField(max_length=20, null=True, blank=True)

    street_address1 = models.CharField(max_length=80, null=False, blank=False)

    street_address2 = models.CharField(max_length=80, null=True, blank=True)

    city_or_town = models.CharField(max_length=80, null=False, blank=False)

    county_or_state = models.CharField(
        max_length=80, null=True, blank=True)

    postcode = models.CharField(max_length=25, null=False, blank=False)

    country = CountryField(blank_label='Country *', null=False, blank=False)

    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)

    item_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _create_order_number(self):
        prefix = '#HH'
        unique_id = uuid.uuid4().hex[:6].upper()
        return prefix + unique_id

    def update_total(self):
        self.item_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.item_total < settings.FREE_SHIPPING_THRESHOLD:
            self.delivery_cost = settings.STANDARD_SHIPPING_FEE
        else:
            self.delivery_cost = 0
        self.order_total = float(self.item_total) + float(self.delivery_cost)
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')

    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)

    variant = models.ForeignKey(
        Variant, blank=True, null=True, on_delete=models.CASCADE)

    quantity = models.IntegerField(
        blank=False, null=False, default=0)

    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        if self.variant:
            self.lineitem_total = self.variant.price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity

        super().save(*args, **kwargs)

    def __str__(self):
        if self.variant:
            return f'{self.product.name}-{self.variant.name}'
        else:
            return f'{self.product.name}'
