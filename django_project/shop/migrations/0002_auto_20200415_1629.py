# Generated by Django 3.0.4 on 2020-04-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(default='New', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
