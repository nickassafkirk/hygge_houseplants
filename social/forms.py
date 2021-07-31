from django import forms
from .models import SocialMediaProfile


class SocialForm(forms.ModelForm):

    class Meta:
        model = SocialMediaProfile
        fields = '__all__'
