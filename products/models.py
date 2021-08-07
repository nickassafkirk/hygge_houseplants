from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    sku = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(null=False, default=1)
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    has_variants = models.BooleanField(default=False, null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Variant(models.Model):

    parent_product = models.ForeignKey(
        Product,
        related_name='variants',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    name = models.CharField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=50, null=True, blank=True)

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
        )

    color = models.CharField(max_length=25, null=True, blank=True)
    size = models.CharField(max_length=4, null=True, blank=True)
    quantity = models.IntegerField(null=False, default=0)
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
