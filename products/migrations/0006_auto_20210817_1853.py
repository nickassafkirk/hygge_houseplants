# Generated by Django 3.2.6 on 2021-08-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210817_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='display_name',
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]