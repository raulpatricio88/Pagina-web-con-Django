# Generated by Django 5.0.1 on 2024-01-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='imagen'),
        ),
    ]
