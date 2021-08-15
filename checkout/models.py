from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

from products.models import Product, Variant


class Order(models.Model):
    order_number = models.CharField(max_length=25, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    emails = models.EmailField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, False=True)