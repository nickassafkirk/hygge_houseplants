# Generated by Django 3.2.6 on 2021-08-17 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210816_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_Address1',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_Address2',
            new_name='street_address2',
        ),
    ]
