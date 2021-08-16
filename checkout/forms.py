from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    model = Order
    fields = (
        'full_name',
        'email',
        'phone_number',
        'street_Address1',
        'street_Address1',
        'city_or_town',
        'county_or_state',
        'postcode',
        'country',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'city_or_town': 'Town/City',
            'county_or_state': 'County/State',
            'postcode': 'Postcode',
            'country': 'Country',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False
