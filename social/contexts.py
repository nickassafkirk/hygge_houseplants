from .models import SocialMediaProfile


def social(request):
    social_accounts = SocialMediaProfile.objects.all()
    context = {
        'social_accounts': social_accounts,
    }
    return context
