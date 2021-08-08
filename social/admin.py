from django.contrib import admin
from .models import SocialMediaProfile


class SocialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'link',
    )


admin.site.register(SocialMediaProfile, SocialAdmin)
