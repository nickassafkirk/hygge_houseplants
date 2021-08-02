from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

        name = models.Charfield(max_length=254)
        formatted_name = models.Charfield(max_length=254, null=True, blank=True)

        def __str__(self):
            return self.name

        def  get_formatted_name(self):
            return self.formatted_name



