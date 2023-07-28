# Generated by Django 3.2.14 on 2023-07-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("service_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceapi",
            name="header",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="serviceapi",
            name="action",
            field=models.CharField(
                choices=[
                    ("ADDRESS_VALIDATION", "Address Validation"),
                    ("SHIPPING", "Shipping"),
                    ("CANCEL_SHIPMENT", "Cancel Shipping"),
                    ("LOGIN", "Login"),
                ],
                max_length=255,
            ),
        ),
    ]
