# Generated by Django 3.2.15 on 2024-01-26 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0041_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderelement',
            options={'verbose_name': 'Элемент заказа', 'verbose_name_plural': 'Элементы заказа'},
        ),
    ]
