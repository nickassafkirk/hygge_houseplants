from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import SocialForm, IconForm
from .models import SocialMediaProfile


@login_required
def add_social_account(request):
    if not request.user.is_superuser:
        messages.error(request,"Site admin access only!")
        return redirect(reverse('home'))
    if request.method == "POST":

        form2 = SocialForm(request.POST)
        if form2.is_valid():
            form2.save()
            messages.success(request, 'Social accounts updated successfully!')
            return redirect(reverse('edit_social_account'))
        else:
            messages.error(request, "Invalid form. Check values and retry")
    else:
        form2 = SocialForm()
    template = 'social/add_social.html'
    context = {
        'form2':form2,
    }

    return render(request, template, context)


@login_required
def edit_social_account(request):
    if not request.user.is_superuser:
        messages.error(request,"Site admin access only!")
        return redirect(reverse('home'))
    FormSet = modelformset_factory(
        SocialMediaProfile,
        form=SocialForm,
        extra=0,
        can_delete=True,
        can_delete_extra=False,
        )

    if request.method == "POST":

        formset = FormSet(request.POST)
        print('formset check valid')

        for form in formset:
            print(form.has_changed())
            if form.has_changed():
                if form.is_valid():
                    form.save()
                else:
                    messages.error(request, "Invalid form. Check values and retry")

        deleted_forms = formset.deleted_forms
        print(deleted_forms)
        if deleted_forms:
            for account_to_delete in deleted_forms:
                id = int(account_to_delete['id'].value())
                print(id)
                delete_account(id)

        messages.success(request, 'Social accounts updated successfully!')
        return redirect(reverse('edit_social_account'))

    else:
        formset = FormSet()

        template = 'social/edit_social.html'
        context = {
            'formset': formset,
        }
        return render(request, template, context)


@login_required
def delete_account(pk):
    if not request.user.is_superuser:
        messages.error(request,"Site admin access only!")
        return redirect(reverse('home'))
    account = get_object_or_404(SocialMediaProfile, pk=pk)
    print('delete called', account)
    account.delete()


@login_required
def add_icon(request):
    if not request.user.is_superuser:
        messages.error(request,"Site admin access only!")
        return redirect(reverse('home'))

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
