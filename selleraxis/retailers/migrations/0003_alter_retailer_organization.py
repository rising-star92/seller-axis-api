# Generated by Django 3.2.14 on 2023-07-21 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0003_auto_20230706_0702"),
        ("retailers", "0002_auto_20230706_0832"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailer",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="retailer_organization",
                to="organizations.organization",
            ),
        ),
    ]
