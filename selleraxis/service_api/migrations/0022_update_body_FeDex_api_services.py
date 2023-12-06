# Generated by Django 3.2.14 on 2023-10-10 17:54

from django.db import migrations

from selleraxis.service_api.models import ServiceAPI
from selleraxis.services.models import Services


def update_body_fedex(apps, schema_editor):
    fedex = Services.objects.filter(name="FEDEX").first()
    ServiceAPI.objects.filter(service=fedex, action="CANCEL_SHIPMENT").update(
        body="""{
            "accountNumber": {
                "value": "{{carrier.account_number}}"
            },
            "trackingNumber": "{{tracking_number}}"
        }"""
    )


class Migration(migrations.Migration):
    dependencies = [
        ("service_api", "0021_update_shipping_fedex_body"),
    ]

    operations = [migrations.RunPython(update_body_fedex)]