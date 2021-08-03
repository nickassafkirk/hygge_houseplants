from django import forms
from .widgets import CustomClearableFileInput


from .models import Product, Category, Variant


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('created_date',)

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)
    has_variants = forms.BooleanField(required=False)
    available = forms.BooleanField(required=True, initial=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(category.id, category.get_display_name()) for category in categories]

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
        fields = '__all__'

