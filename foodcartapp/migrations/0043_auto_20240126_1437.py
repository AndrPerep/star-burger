# Generated by Django 3.2.15 on 2024-01-26 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0042_alter_orderelement_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderelement',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodcartapp.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderelement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodcartapp.product', verbose_name='Продукт'),
        ),
    ]