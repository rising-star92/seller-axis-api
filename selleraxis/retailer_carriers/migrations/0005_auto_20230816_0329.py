# Generated by Django 3.2.14 on 2023-08-16 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0005_set_default_email"),
        ("services", "0003_services_shipment_tracking_url"),
        ("retailer_carriers", "0004_remove_retailercarrier_is_default"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="retailercarrier",
            name="retailer",
        ),
        migrations.AddField(
            model_name="retailercarrier",
            name="organization",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organizations",
                to="organizations.organization",
            ),
        ),
        migrations.AlterField(
            model_name="retailercarrier",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="retailer_carrier_services",
                to="services.services",
            ),
        ),
    ]