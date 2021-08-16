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
    )

    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'street_Address1',
        'street_Address2',
        'city_or_town',
        'state_or_province',
        'postcode',
        'country',
        'delivery_cost',
        'item_total',
        'order_total',
    )

    ordering = ('order_number',)


admin.site.register(Order, OrderAdmin)
