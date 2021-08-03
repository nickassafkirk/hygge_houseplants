from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label="Email")
    name = forms.CharField(label="Name", required=False)
    phone = forms.IntegerField(max_value=15, required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
