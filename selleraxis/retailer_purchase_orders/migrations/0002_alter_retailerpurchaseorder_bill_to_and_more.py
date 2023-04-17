# Generated by Django 4.1.7 on 2023-03-31 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("retailer_participating_parties", "0001_initial"),
        ("retailer_person_places", "0001_initial"),
        ("retailer_purchase_orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="bill_to",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bill_to_orders",
                to="retailer_person_places.retailerpersonplace",
            ),
        ),
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customer_orders",
                to="retailer_person_places.retailerpersonplace",
            ),
        ),
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="invoice_to",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice_to_orders",
                to="retailer_person_places.retailerpersonplace",
            ),
        ),
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="participating_party",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="retailer_participating_parties.retailerparticipatingparty",
            ),
        ),
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="ship_to",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ship_to_orders",
                to="retailer_person_places.retailerpersonplace",
            ),
        ),
    ]