# Generated by Django 3.0.4 on 2020-04-23 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200423_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
    ]
