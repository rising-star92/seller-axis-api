# Generated by Django 3.2.14 on 2023-08-18 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("retailer_warehouses", "0004_auto_20230814_0814"),
        ("retailer_carriers", "0005_auto_20230816_0329"),
        ("retailers", "0009_auto_20230816_0449"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailer",
            name="default_carrier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="retailer_carrier",
                to="retailer_carriers.retailercarrier",
            ),
        ),
        migrations.AlterField(
            model_name="retailer",
            name="default_warehouse",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="retailer_warehouse",
                to="retailer_warehouses.retailerwarehouse",
            ),
        ),
    ]
