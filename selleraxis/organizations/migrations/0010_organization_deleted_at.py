# Generated by Django 3.2.14 on 2023-10-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0009_add_qbo_token_info_2"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
