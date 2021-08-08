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

    def __init__(self, *args, **kwargs):
        super(SocialForm, self).__init__(*args, **kwargs)
        icons = SocialMediaIcon.objects.all()
        display_names = [(i.id, i.name) for i in icons]

        self.fields['icon'].choices = display_names
