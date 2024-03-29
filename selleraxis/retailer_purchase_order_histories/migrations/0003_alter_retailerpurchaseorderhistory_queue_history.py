# Generated by Django 3.2.14 on 2023-11-10 11:09

from django.db import migrations, models
import django.db.models.deletion
from selleraxis.retailer_purchase_order_histories.models import (
    RetailerPurchaseOrderHistory,
)
from selleraxis.retailer_purchase_orders.models import RetailerPurchaseOrder


def update_missing_history(app, app_schema):
    orders = RetailerPurchaseOrder.objects.all().distinct("id")
    list_create_historys = []
    for order in orders:
        if not RetailerPurchaseOrderHistory.objects.filter(
            order=order.id,
            status="Opened",
        ).exists():
            list_create_historys.append(
                RetailerPurchaseOrderHistory(status="Opened", order=order)
            )
        match order.status:
            case "Acknowledged" | "Backorder" | "Bypassed Acknowledge":
                if not RetailerPurchaseOrderHistory.objects.filter(
                    order=order.id,
                    status=order.status,
                ).exists():
                    list_create_historys.append(
                        RetailerPurchaseOrderHistory(status=order.status, order=order)
                    )
            case "Shipped" | "Partly Shipped" | "Cancelled":
                if not RetailerPurchaseOrderHistory.objects.filter(
                    order=order.id,
                    status="Acknowledged",
                ).exists():
                    list_create_historys.append(
                        RetailerPurchaseOrderHistory(status="Acknowledged", order=order)
                    )
                list_create_historys.append(
                    RetailerPurchaseOrderHistory(status=order.status, order=order)
                )
            case "Shipment Confirmed":
                list_status = ["Acknowledged", "Shipped", order.status]
                for status in list_status:
                    if not RetailerPurchaseOrderHistory.objects.filter(
                        order=order.id,
                        status=status,
                    ).exists():
                        list_create_historys.append(
                            RetailerPurchaseOrderHistory(status=status, order=order)
                        )
            case "Partly Shipped Confirmed":
                list_status = ["Acknowledged", "Partly Shipped", order.status]
                for status in list_status:
                    if not RetailerPurchaseOrderHistory.objects.filter(
                        order=order.id,
                        status=status,
                    ).exists():
                        list_create_historys.append(
                            RetailerPurchaseOrderHistory(status=status, order=order)
                        )
            case "Invoiced":
                list_status = ["Acknowledged", "Shipped", order.status]
                for status in list_status:
                    if not RetailerPurchaseOrderHistory.objects.filter(
                        order=order.id,
                        status=status,
                    ).exists():
                        list_create_historys.append(
                            RetailerPurchaseOrderHistory(status=status, order=order)
                        )
            case "Invoice Confirmed":
                list_status = [
                    "Acknowledged",
                    "Shipped",
                    "Invoiced",
                    "Invoice Confirmed",
                ]
                for status in list_status:
                    if not RetailerPurchaseOrderHistory.objects.filter(
                        order=order.id,
                        status=status,
                    ).exists():
                        list_create_historys.append(
                            RetailerPurchaseOrderHistory(status=status, order=order)
                        )
    RetailerPurchaseOrderHistory.objects.bulk_create([*list_create_historys])


class Migration(migrations.Migration):
    dependencies = [
        ("retailer_queue_histories", "0005_alter_retailerqueuehistory_label"),
        (
            "retailer_purchase_order_histories",
            "0002_alter_retailerpurchaseorderhistory_status",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="retailerpurchaseorderhistory",
            name="queue_history",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_queue_history",
                to="retailer_queue_histories.retailerqueuehistory",
            ),
        ),
        migrations.RunPython(update_missing_history),
    ]
