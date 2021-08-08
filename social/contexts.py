from .models import SocialMediaProfile, SocialMediaIcon


def social(request):
    social_accounts = SocialMediaProfile.objects.all()
    social_icons = SocialMediaIcon.objects.all()
    context = {
        'social_accounts': social_accounts,
        'icons': social_icons,
    }
    return context
