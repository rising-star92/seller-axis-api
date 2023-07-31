# Generated by Django 3.2.14 on 2023-07-31 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("retailer_carriers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RetailerShipper",
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
                ("name", models.CharField(max_length=100)),
                ("attention_name", models.CharField(max_length=100)),
                ("tax_identification_number", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=100)),
                ("shipper_number", models.CharField(max_length=100)),
                ("fax_number", models.CharField(max_length=150)),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=150)),
                ("state", models.CharField(max_length=150)),
                ("postal_code", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=150)),
                ("company", models.CharField(max_length=150)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "retailer_carrier",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retailer_carriers.retailercarrier",
                    ),
                ),
            ],
        ),
    ]
