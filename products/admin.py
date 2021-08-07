from django.contrib import admin
from .models import Category, Product, Variant


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sku',
        'category',
        'price',
        'image',
        'available',
    )

    ordering = ('id',)


class VariantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'parent_product',
        'name',
        'sku',
        'price',
        'image',
        'quantity'
    )

    ordering = ('parent_product',)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
