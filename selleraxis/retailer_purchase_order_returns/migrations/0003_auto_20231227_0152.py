# Generated by Django 3.2.14 on 2023-12-27 06:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("retailer_purchase_order_returns", "0002_auto_20231214_0347"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="retailerpurchaseorderreturn",
            name="dispute_date",
        ),
        migrations.RemoveField(
            model_name="retailerpurchaseorderreturn",
            name="is_dispute",
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="dispute_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="dispute_reason",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="dispute_result",
            field=models.CharField(
                choices=[
                    ("REFUNDED_NOT_RETURNED", "Refunded Not Returned"),
                    ("REFUNDED_AFTER_RETURN", "Refunded After Return"),
                    ("REJECTED_FULL_PAYMENT", "Rejected Full Payment"),
                    ("REJECTED_RETURN_SHIP", "Rejected Return Ship"),
                    ("REFUNDED_BOTH_PARTIES", "Refunded Both Parties"),
                ],
                default=None,
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="dispute_status",
            field=models.CharField(
                choices=[
                    ("Dispute requested", "Dispute requested"),
                    ("Dispute denied", "Dispute denied"),
                    ("Dispute reimbursed", "Dispute reimbursed"),
                ],
                default=None,
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="reimbursed_amount",
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="service",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="status",
            field=models.CharField(
                choices=[
                    ("Return opened", "Return opened"),
                    ("Return receive", "Return receive"),
                ],
                default="Return opened",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="tracking_number",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="retailerpurchaseorderreturn",
            name="updated_dispute_at",
            field=models.DateTimeField(null=True),
        ),
    ]
