# Generated by Django 3.2.14 on 2023-08-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("retailer_purchase_orders", "0015_alter_retailerpurchaseorder_order_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="status",
            field=models.CharField(
                choices=[
                    ("Opened", "Opened"),
                    ("Acknowledged", "Acknowledged"),
                    ("Shipped", "Shipped"),
                    ("Shipment Confirmed", "Shipment Confirmed"),
                    ("Invoiced", "Invoiced"),
                    ("Invoice Confirmed", "Invoice Confirmed"),
                    ("Cancelled", "Cancelled"),
                    ("Bypassed Acknowledge", "Bypassed Acknowledge"),
                ],
                default="Opened",
                max_length=255,
            ),
        ),
    ]
