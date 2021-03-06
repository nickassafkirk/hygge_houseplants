# Generated by Django 3.2.5 on 2021-07-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('link', models.URLField(blank=True, max_length=1024, null=True)),
                ('icon', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
