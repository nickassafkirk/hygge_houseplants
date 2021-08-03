from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import SocialForm


def add_social_account(request):
    if request.method == "POST":
        form = SocialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('social'))
        else:
            print('form is invalid')
    else:
        form = SocialForm()

    template = 'social/add_social.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
