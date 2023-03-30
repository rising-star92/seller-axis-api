# Generated by Django 3.2.14 on 2023-03-30 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("retailer_person_places", "0001_initial"),
        ("retailer_participating_parties", "0001_initial"),
        ("retailer_order_batchs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RetailerPurchaseOrder",
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
                ("retailer_purchase_order_id", models.CharField(max_length=255)),
                ("transaction_id", models.CharField(max_length=255)),
                ("senders_id_for_receiver", models.CharField(max_length=255)),
                ("po_number", models.CharField(max_length=255)),
                ("order_date", models.DateTimeField(auto_now=True)),
                ("shipping_code", models.CharField(max_length=255)),
                ("sales_division", models.CharField(max_length=255)),
                ("vendor_warehouse_id", models.CharField(max_length=255)),
                ("cust_order_number", models.CharField(max_length=255)),
                ("po_hdr_data", models.JSONField()),
                ("control_number", models.CharField(max_length=255)),
                ("buying_contract", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "batch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retailer_order_batchs.retailerorderbatch",
                    ),
                ),
                (
                    "bill_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bill_to_orders",
                        to="retailer_person_places.retailerpersonplace",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer_orders",
                        to="retailer_person_places.retailerpersonplace",
                    ),
                ),
                (
                    "invoice_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice_to_orders",
                        to="retailer_person_places.retailerpersonplace",
                    ),
                ),
                (
                    "participating_party",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retailer_participating_parties.retailerparticipatingparty",
                    ),
                ),
                (
                    "ship_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ship_to_orders",
                        to="retailer_person_places.retailerpersonplace",
                    ),
                ),
            ],
        ),
    ]
