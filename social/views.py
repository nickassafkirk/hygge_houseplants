from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import SocialForm, IconForm
from .models import SocialMediaProfile


def edit_social_account(request):
    FormSet = modelformset_factory(
        SocialMediaProfile,
        form=SocialForm,
        extra=0,
        can_delete=True,
        )

    if request.method == "POST":
        formset = FormSet(request.POST)
        print('formset check valid')
        if formset.is_valid():
            formset = formset.save()
            print('formset saved')
            messages.success(request, 'Social accounts updated successfully!')   
        else:
            print(formset.non_form_errors())
            print(formset.errors)
            messages.error(request, 'invalid formset')
        return redirect(reverse('edit_social_account'))
    else:
        formset = FormSet()

        template = 'social/edit_social.html'
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
