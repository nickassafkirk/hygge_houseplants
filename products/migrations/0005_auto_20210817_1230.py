# Generated by Django 3.2.6 on 2021-08-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='products',
        ),
        migrations.AddField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
