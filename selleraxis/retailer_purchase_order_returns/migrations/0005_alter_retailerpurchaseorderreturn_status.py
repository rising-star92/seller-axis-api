# Generated by Django 3.2.14 on 2024-01-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "retailer_purchase_order_returns",
            "0004_retailerpurchaseorderreturn_dispute_id",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailerpurchaseorderreturn",
            name="status",
            field=models.CharField(
                choices=[
                    ("Return opened", "Return opened"),
                    ("Return received", "Return received"),
                ],
                default="Return opened",
                max_length=100,
                null=True,
            ),
        ),
    ]
