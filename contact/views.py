from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            # Add name and phone to message body if defined
            if form.cleaned_data['name'] and form.cleaned_data['phone']:
                message = f'Name: {form.cleaned_data["name"]}\nPhone: {form.cleaned_data["phone"]}\n' + message
            elif form.cleaned_data['name']:
                message = f'Name: {form.cleaned_data["name"]}\n' + message
            elif form.cleaned_data['phone']:
                message = f'Phone: {form.cleaned_data["phone"]}\n' + message
            else:
                message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['nickassafkirk@gmail.com'],)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')

    return render(request, "contact/contact.html", {'form': form})

def contact_success(request):
    return HttpResponse('Success! Thank you for your message.')
