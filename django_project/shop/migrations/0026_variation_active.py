# Generated by Django 3.0.4 on 2020-05-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200530_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
