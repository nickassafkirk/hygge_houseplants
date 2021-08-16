from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    This method updates the cart total when a lineitem is edited
    sender is sender of signal,
    instance is instance of model,
    created is bool val to say if instance is new or to be updates,
    keywords handle additional arguements.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the cart total when lineitem is deleted
    """
    instance.order.update_total()
