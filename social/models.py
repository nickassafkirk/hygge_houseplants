from django.db import models


class SocialMediaIcon(models.Model):
    name = models.CharField(max_length=25)
    logo = models.CharField(max_length=50)


class SocialMediaProfile(models.Model):
    name = models.CharField(max_length=25)
    link = models.URLField(max_length=1024, null=True, blank=True)
    icon = models.ForeignKey(
        SocialMediaIcon,
        related_name='icon',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
