from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.forms import modelformset_factory
from .forms import SocialForm, IconForm
from .models import SocialMediaProfile


def add_social_account(request):
    FormSet = modelformset_factory(
        SocialMediaProfile,
        form=SocialForm,
        extra=1,
        can_delete=True,
        )
    if request.method == "POST":
        form = SocialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('form is invalid')
    else:
        formset = FormSet()

    template = 'social/add_social.html'
    context = {
        'formset': formset,
    }
    return render(request, template, context)


def add_icon(request):

    if request.method == "POST":

        form = IconForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_icon')
        else:
            print('form is invalid')
    else:
        form = IconForm()

    template = 'social/add_icon.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
