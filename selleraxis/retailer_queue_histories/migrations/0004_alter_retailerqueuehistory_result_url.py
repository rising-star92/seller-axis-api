# Generated by Django 3.2.14 on 2023-08-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("retailer_queue_histories", "0003_retailerqueuehistory_label"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailerqueuehistory",
            name="result_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
