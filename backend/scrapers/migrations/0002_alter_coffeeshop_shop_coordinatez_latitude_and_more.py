# Generated by Django 5.0 on 2023-12-19 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeshop',
            name='shop_coordinatez_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='coffeeshop',
            name='shop_coordinatez_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]