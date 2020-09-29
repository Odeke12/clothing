# Generated by Django 3.0.4 on 2020-06-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_variation_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='title',
        ),
        migrations.AddField(
            model_name='variation',
            name='color',
            field=models.CharField(choices=[('R', 'Red'), ('B', 'Black'), ('Y', 'Yellow'), ('P', 'Pink')], default='R', max_length=2),
        ),
        migrations.AddField(
            model_name='variation',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='M', max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shoes'), ('H', 'Shirts'), ('I', 'Shorts'), ('T', 'Trousers'), ('P', 'Pyjamas')], default='Pick a category', max_length=20),
        ),
        migrations.AlterField(
            model_name='variation',
            name='image',
            field=models.ImageField(default='product.image1', upload_to='product_pics'),
        ),
    ]