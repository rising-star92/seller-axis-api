# Generated by Django 4.2.3 on 2023-07-28 03:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order_package", "0003_auto_20230727_0402"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderpackage",
            name="weight_unit",
            field=models.CharField(
                choices=[("LB", "lb"), ("LBS", "lbs"), ("KG", "kg")],
                default="lb",
                max_length=100,
            ),
        ),
    ]
