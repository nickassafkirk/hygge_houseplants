from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

        name = models.CharField(max_length=254)
        formatted_name = models.CharField(
            max_length=254, null=True, blank=True)

        def __str__(self):
            return self.name

        def get_formatted_name(self):
            return self.formatted_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(max_length=6)
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    has_variants = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
