from django import forms
from .widgets import CustomClearableFileInput
from django.utils.translation import ugettext_lazy as _

from .models import Product, Category, Variant, Collection


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ('name', 'description', 'products', 'active',)

    name = forms.CharField(max_length=80)

    description = forms.Textarea()

    products = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Product.objects.all(),
    )

    active = forms.BooleanField(initial=True)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_date',)

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput)
    has_variants = forms.BooleanField(required=False)
    available = forms.BooleanField(required=True, initial=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [
            (category.id, category.get_display_name())
            for category in categories
            ]

        cat_field = self.fields['category']
        variants_field = self.fields['has_variants']

        variants_field.widget.attrs['id'] = "has_variants"

        cat_field.choices = display_names
        cat_field.widget.attrs.update({'class': 'form-select'})
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'product-form-field'


class VariantForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = (
            'parent_product', 'color', 'size', 'price',
            'quantity', 'image',
            )
        labels = {
            'parent_product': _(''),
            'name': _(''),
            'sku': _('Variant Sku'),
            'price': _('Variant Price'),
            'quantity': _('Variant Quantity'),
            'image': _('Variant Image'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = []
        form_fields = self.fields.items()
        for key, val in form_fields:
            label = "Variant " + key.capitalize()
            labels.append(label)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"

        parent_product = self.fields['parent_product']
        parent_product.widget.attrs['class'] = "d-none"
