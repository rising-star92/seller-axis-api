# Generated by Django 4.2.3 on 2023-07-27 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("boxes", "0004_alter_box_max_quantity"),
        ("package_rules", "0007_alter_packagerule_product_series"),
    ]

    operations = [
        migrations.AlterField(
            model_name="packagerule",
            name="box",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="package_rules",
                to="boxes.box",
            ),
        ),
    ]
