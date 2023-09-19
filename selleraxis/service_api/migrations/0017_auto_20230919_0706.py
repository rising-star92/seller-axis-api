# Generated by Django 3.2.14 on 2023-09-19 11:06

from django.db import migrations
from selleraxis.service_api.models import ServiceAPI
from selleraxis.services.models import Services


def set_default_fedex_client(apps, schema_editor):
    fedex = Services.objects.filter(name="FEDEX").first()
    fedex_service = ServiceAPI.objects.filter(
        service=fedex, action="ADDRESS_VALIDATION"
    ).first()
    fedex_service.response = """{
        "address_1": "{{output.resolvedAddresses.0.streetLinesToken.0}}",
        "address_2": "{{output.resolvedAddresses.0.streetLinesToken.1}}",
        "city": "{{output.resolvedAddresses.0.city}}",
        "state": "{{output.resolvedAddresses.0.stateOrProvinceCode}}",
        "postal_code": "{{output.resolvedAddresses.0.postalCode}}",
        "country": "{{output.resolvedAddresses.0.countryCode}}",
        "classification": "{{output.resolvedAddresses.0.classification}}"
    }"""
    fedex_service.save()


class Migration(migrations.Migration):
    dependencies = [
        ("service_api", "0016_auto_20230918_2305"),
    ]

    operations = [migrations.RunPython(set_default_fedex_client)]
