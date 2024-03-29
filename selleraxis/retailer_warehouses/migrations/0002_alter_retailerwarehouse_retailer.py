# Generated by Django 3.2.14 on 2023-07-13 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("retailers", "0002_auto_20230706_0832"),
        ("retailer_warehouses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailerwarehouse",
            name="retailer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="retailer_warehouses",
                to="retailers.retailer",
            ),
        ),
    ]
