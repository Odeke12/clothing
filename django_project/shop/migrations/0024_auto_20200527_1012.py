# Generated by Django 3.0.4 on 2020-05-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_itemreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='cat',
            field=models.ManyToManyField(blank='True', null='True', to='shop.Category'),
            preserve_default='True',
        ),
    ]