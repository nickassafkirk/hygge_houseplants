from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import SocialMediaProfile
from .forms import SocialForm


def social(request):
    social_accounts = SocialMediaProfile.objects.all()
    context = {
        'social_accounts': social_accounts,
    }
    return render(request, 'social/social.html', context)


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
