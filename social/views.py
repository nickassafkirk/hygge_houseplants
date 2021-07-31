from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import SocialMediaProfile



def social(request):
    social_accounts = SocialMediaProfile.objects.all()
    context = {
        'social_accounts': social_accounts,
    }
    return render(request, 'social/social.html', context)


