# Generated by Django 3.2.14 on 2023-08-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("retailers", "0007_auto_20230814_1048"),
    ]

    operations = [
        migrations.AddField(
            model_name="retailer",
            name="vendor_id",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
