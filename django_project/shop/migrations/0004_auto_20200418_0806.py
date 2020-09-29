# Generated by Django 3.0.4 on 2020-04-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200416_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shoes'), ('H', 'Shirts'), ('I', 'Shorts'), ('T', 'Trousers')], default='Pick a category', max_length=20),
        ),
    ]
