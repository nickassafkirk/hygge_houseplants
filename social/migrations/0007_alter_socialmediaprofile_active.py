# Generated by Django 3.2.6 on 2021-08-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_alter_socialmediaprofile_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediaprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]