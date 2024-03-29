# Generated by Django 3.2.14 on 2023-12-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("retailer_purchase_order_returns", "0001_initial"),
        ("retailer_purchase_order_return_items", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="retailerpurchaseorderreturnitem",
            name="order_return",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_returns_items",
                to="retailer_purchase_order_returns.retailerpurchaseorderreturn",
            ),
        ),
    ]
