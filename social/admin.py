from django.contrib import admin
from .models import SocialMediaProfile, SocialMediaIcon


class SocialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'link',
    )


class IconAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'icon',
    )


admin.site.register(SocialMediaProfile, SocialAdmin)
admin.site.register(SocialMediaIcon, IconAdmin)
