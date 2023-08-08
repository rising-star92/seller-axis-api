# Generated by Django 3.2.14 on 2023-08-08 08:51

from django.db import migrations, models
import django.db.models.deletion
from selleraxis.shipping_service_types.models import ShippingServiceType
from selleraxis.services.models import Services


def migrate_shipping_service_type(apps, schema_editor):
    fedex_data = {
        "FedEx International Priority Express": "FEDEX_INTERNATIONAL_PRIORITY_EXPRESS",
        "FedEx International First": "INTERNATIONAL_FIRST",
        "FedEx International Priority": "FEDEX_INTERNATIONAL_PRIORITY",
        "FedEx International Economy": "INTERNATIONAL_ECONOMY",
        "FedEx International Ground": "FEDEX_GROUND",
        "FedEx International MailService": "FEDEX_CARGO_MAIL",
        "FedEx International Premium": "FEDEX_CARGO_INTERNATIONAL_PREMIUM",
        "FedEx First Overnight": "FIRST_OVERNIGHT",
        "FedEx First Overnight Freight": "FIRST_OVERNIGHT_FREIGHT",
        "FedEx 1Day Freight": "FEDEX_1_DAY_FREIGHT",
        "FedEx 2Day Freight": "FEDEX_2_DAY_FREIGHT",
        "FedEx 3Day Freight": "FEDEX_3_DAY_FREIGHT",
        "FedEx International Priority Freight": "INTERNATIONAL_PRIORITY_FREIGHT",
        "FedEx International Economy Freight": "INTERNATIONAL_ECONOMY_FREIGHT",
        "FedEx International Express Freight and FedEx International Airport-to-Airport": "FEDEX_CARGO_AIRPORT_TO_AIRPORT",
        "FedEx International Priority DirectDistribution": "INTERNATIONAL_PRIORITY_DISTRIBUTION",
        "FedEx International Priority DirectDistribution Freight": "FEDEX_IP_DIRECT_DISTRIBUTION_FREIGHT",
        "International Ground Distribution (IGD)": "INTL_GROUND_DISTRIBUTION",
        "FedEx Home Delivery": "GROUND_HOME_DELIVERY",
        "FedEx Ground Economy (Formerly known as FedEx SmartPost)": "SMART_POST",
        "FedEx Priority Overnigh": "PRIORITY_OVERNIGHT",
        "FedEx Standard Overnight(Hawaii outbound only)": "STANDARD_OVERNIGHT",
        "FedEx 2Day(Except Intra-Hawaii)": "FEDEX_2_DAY",
        "FedEx 2Day AM(Hawaii outbound only)": "FEDEX_2_DAY_AM",
        "FedEx Express Saver(Except Alaska and Hawaii)": "FEDEX_EXPRESS_SAVER",
        "FedEx SameDay": "SAME_DAY",
        "FedEx SameDay City(Selected U.S. Metro Areas)": "SAME_DAY_CITY",
    }
    ups_data = {
        "Next Day Air": "01",
        "2nd Day Air": "02",
        "Ground": "03",
        "Express": "07",
        "Expedited": "08",
        "UPS Standard": "11",
        "3 Day Select": "12",
        "Next Day Air Saver": "13",
        "UPS Next Day Air Early": "14",
        "UPS Worldwide Economy DDU": "17",
        "Express Plus": "54",
        "2nd Day Air A.M.": "59",
        "UPS Saver": "65",
        "First Class Mail": "M2",
        "Priority Mail": "M3",
        "Expedited MaiI Innovations": "M4",
        "Priority Mail Innovations": "M5",
        "Economy Mail Innovations": "M6",
        "MaiI Innovations (MI) Returns": "M7",
        "UPS Access Point Economy": "70",
        "UPS Worldwide Express Freight Midday": "71",
        "UPS Worldwide Economy DDP": "72",
        "UPS Express 12:00": "74",
        "UPS Heavy Goods": "75",
        "UPS Today Standard": "82",
        "UPS Today Dedicated Courier": "83",
        "UPS Today Intercity": "84",
        "UPS Today Express": "85",
        "UPS Today Express Saver": "86",
        "UPS Worldwide Express Freight": "96",
    }
    type_list = []
    datas = Services.objects.filter(name__in=["UPS", "FEDEX"])
    for data in datas:
        if data.name == "UPS":
            for name, code in ups_data.items():
                type_list.append(
                    ShippingServiceType(
                        name=name,
                        code=code,
                        service=data,
                    )
                )
        if data.name == "FEDEX":
            for name, code in fedex_data.items():
                type_list.append(
                    ShippingServiceType(
                        name=name,
                        code=code,
                        service=data,
                    )
                )
    ShippingServiceType.objects.bulk_create(type_list)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("services", "0003_services_shipment_tracking_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingServiceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=155)),
                ("code", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "service",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="shipping_services",
                        to="services.services",
                    ),
                ),
            ],
        ),
        migrations.RunPython(migrate_shipping_service_type),
    ]
