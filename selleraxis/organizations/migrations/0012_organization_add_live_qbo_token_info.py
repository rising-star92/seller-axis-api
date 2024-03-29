# Generated by Django 3.2.14 on 2023-10-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0011_organization_is_sandbox"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="live_qbo_access_token",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="live_qbo_access_token_exp_time",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="live_qbo_refresh_token",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="live_qbo_refresh_token_exp_time",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="live_realm_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
