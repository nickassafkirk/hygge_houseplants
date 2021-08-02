from django import forms


from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Product Name',
            'category': 'Product Category',
            'sku': 'Product SKU',
            'description': 'Description',
            'price': 'Price(€)',
            'quantity': 'Stock Quantity',
            'image_url': 'Image URL',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image' or field != 'has_variants' or field != 'available':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'product-form-field'
            self.fields[field].label = False
