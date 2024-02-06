# Generated by Django 3.2.15 on 2024-01-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0038_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=None, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.TextField(default=None, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]