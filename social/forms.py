from django import forms
from .models import SocialMediaProfile, SocialMediaIcon


class IconForm(forms.ModelForm):

    class Meta:
        model = SocialMediaIcon
        fields = '__all__'


class SocialForm(forms.ModelForm):

    class Meta:
        model = SocialMediaProfile
        fields = '__all__'
