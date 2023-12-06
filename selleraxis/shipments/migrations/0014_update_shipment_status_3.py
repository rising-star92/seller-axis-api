# Generated by Django 3.2.14 on 2023-11-28 07:15

from django.db import migrations

from selleraxis.retailer_purchase_orders.models import QueueStatus
from selleraxis.shipments.models import ShipmentStatus


def recheck_status(apps, schema_editor):
    # get all order
    RetailerPurchaseOrder = apps.get_model(
        "retailer_purchase_orders", "RetailerPurchaseOrder"
    )
    list_order = RetailerPurchaseOrder.objects.all()

    # get all order package
    OrderPackage = apps.get_model("order_package", "OrderPackage")
    list_order_package = OrderPackage.objects.all()

    # get all order history
    RetailerPurchaseOrderHistory = apps.get_model(
        "retailer_purchase_order_histories", "RetailerPurchaseOrderHistory"
    )
    list_order_history = RetailerPurchaseOrderHistory.objects.all()

    # get all shipment
    Shipment = apps.get_model("shipments", "Shipment")
    list_shipment = Shipment.objects.all()
    list_package_id_shipped = []
    for shipment_item in list_shipment:
        if shipment_item.package is not None:
            list_package_id_shipped.append(shipment_item.package.id)

    for order in list_order:

        # get list package shipped of order
        list_package_for_order = list_order_package.filter(order__id=order.id)
        list_shipment_for_order = list_shipment.filter(
            package__id__in=[package.id for package in list_package_for_order]
        )
        # get list order history of order
        list_order_history_for_order = list_order_history.filter(
            order__id=order.id
        ).order_by("-created_at")

        if order.status in [
            QueueStatus.Invoice_Confirmed.value,
            QueueStatus.Invoiced.value,
            QueueStatus.Shipment_Confirmed.value,
        ]:
            shipment_confirm_latest = None
            for order_history in list_order_history_for_order:
                if (
                    order_history.status.upper()
                    == QueueStatus.Shipment_Confirmed.value.upper()
                ):
                    shipment_confirm_latest = order_history
                    break
            if shipment_confirm_latest is not None:
                Shipment.objects.filter(
                    id__in=[shipment.id for shipment in list_shipment_for_order],
                    created_at__lte=shipment_confirm_latest.created_at,
                    status=ShipmentStatus.CREATED,
                ).update(status=ShipmentStatus.SUBMITTED)
                Shipment.objects.filter(
                    id__in=[shipment.id for shipment in list_shipment_for_order],
                    created_at__gte=shipment_confirm_latest.created_at,
                    status=ShipmentStatus.SUBMITTED,
                ).update(status=ShipmentStatus.CREATED)
            else:
                if order.status in [
                    QueueStatus.Invoice_Confirmed.value,
                    QueueStatus.Shipment_Confirmed.value,
                ]:
                    new_history = RetailerPurchaseOrderHistory(
                        status=QueueStatus.Shipment_Confirmed.value, order=order
                    )
                    new_history.save()
                    Shipment.objects.filter(
                        id__in=[shipment.id for shipment in list_shipment_for_order],
                        status=ShipmentStatus.CREATED,
                    ).update(status=ShipmentStatus.SUBMITTED)
                elif order.status == QueueStatus.Invoiced.value:
                    Shipment.objects.filter(
                        id__in=[shipment.id for shipment in list_shipment_for_order],
                        status=ShipmentStatus.SUBMITTED,
                    ).update(status=ShipmentStatus.CREATED)


class Migration(migrations.Migration):

    dependencies = [
        ("shipments", "0013_update_shipment_status_2"),
    ]

    operations = [
        migrations.RunPython(recheck_status),
    ]