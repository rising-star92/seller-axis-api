# Generated by Django 3.2.14 on 2023-12-11 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("retailer_purchase_order_notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailerpurchaseordernote",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchase_order_note_from",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
