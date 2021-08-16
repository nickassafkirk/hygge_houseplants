from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


def update_on_save(sender, instance, created, **kwargs):
    """
    sender is sender of signal, instance is instance of model, created is bool val to say if
    instance is new or to be updates, keywaords handle additional arguements.
    """