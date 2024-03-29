# Generated by Django 3.2.14 on 2023-08-18 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("organizations", "0008_remove_organization_gs1"),
    ]

    operations = [
        migrations.CreateModel(
            name="GS1",
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
                ("name", models.CharField(max_length=256)),
                ("gs1", models.CharField(max_length=10)),
                ("next_serial_number", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gs1",
                        to="organizations.organization",
                    ),
                ),
            ],
        ),
    ]
