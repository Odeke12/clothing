# Generated by Django 3.0.4 on 2020-05-05 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_billingaddress_home_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='BillingAddress',
            new_name='billing_address',
        ),
    ]
