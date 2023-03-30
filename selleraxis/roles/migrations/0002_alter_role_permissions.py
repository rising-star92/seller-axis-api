# Generated by Django 3.2.14 on 2023-03-30 06:41

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="permissions",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("UPDATE_ORGANIZATION", "Update Organization"),
                        ("DELETE_ORGANIZATION", "Delete Organization"),
                        ("READ_MEMBER", "Read Member"),
                        ("INVITE_MEMBER", "Invite Member"),
                        ("REMOVE_MEMBER", "Remove Member"),
                        ("UPDATE_MEMBER_ROLE", "Update Member Role"),
                        ("CREATE_ROLE", "Create Role"),
                        ("UPDATE_ROLE", "Update Role"),
                        ("DELETE_ROLE", "Delete Role"),
                        ("READ_ROLE", "Read Role"),
                        ("CREATE_RETAILER", "Create Retailer"),
                        ("UPDATE_RETAILER", "Update Retailer"),
                        ("DELETE_RETAILER", "Delete Retailer"),
                        ("READ_RETAILER", "Read Retailer"),
                        ("CREATE_RETAILER_PARTNER", "Create Retailer Partner"),
                        ("UPDATE_RETAILER_PARTNER", "Update Retailer Partner"),
                        ("DELETE_RETAILER_PARTNER", "Delete Retailer Partner"),
                        ("READ_RETAILER_PARTNER", "Read Retailer Partner"),
                        ("CREATE_RETAILER_ORDER_BATCH", "Create Retailer Order Batch"),
                        ("UPDATE_RETAILER_ORDER_BATCH", "Update Retailer Order Batch"),
                        ("DELETE_RETAILER_ORDER_BATCH", "Delete Retailer Order Batch"),
                        ("READ_RETAILER_ORDER_BATCH", "Read Retailer Order Batch"),
                    ],
                    max_length=255,
                ),
                size=None,
            ),
        ),
    ]
