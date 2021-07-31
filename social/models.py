from django.db import models


class SocialMediaProfile(models.Model):
    name = models.CharField(max_length=25)
    link = models.URLField(max_length=1024, null=True, blank=True)
    icon = models.CharField(max_length=20, null=True, blank=True)
