from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm()
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template, context)
