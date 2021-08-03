from django.contrib import admin
from .models import Category, Product


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


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
