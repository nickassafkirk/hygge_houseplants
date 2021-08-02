from django import forms
from .widgets import CustomClearableFileInput


from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_date',)

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'product-form-field'
