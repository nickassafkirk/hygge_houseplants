from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem

    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'item_total',
        'order_total',
        'original_cart',
        'stripe_pid',
    )

    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'city_or_town',
        'county_or_state',
        'postcode',
        'country',
        'delivery_cost',
        'item_total',
        'order_total',
        'original_cart',
        'stripe_pid',
    )

    ordering = ('date',)


admin.site.register(Order, OrderAdmin)
