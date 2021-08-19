from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto generated
        labels and set autofocus on first field
        """

        # We use placeholders to overide default labels for form inputs
        super().__init__(*args, **kwargs)
        labels = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_city_or_town': 'City/Town',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county_or_state': 'County/State',
            'accept_marketing': 'Accept Marketing',
        }

        # set autofocus on full name field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'  # adds a css class