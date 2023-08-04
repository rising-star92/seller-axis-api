from rest_framework.exceptions import ParseError

from selleraxis.order_item_package.models import OrderItemPackage
from selleraxis.order_package.models import OrderPackage
from selleraxis.product_alias.models import ProductAlias


def create_order_package_service(box, order_item, quantity):
    try:
        qty_order = order_item.qty_ordered

        list_ord_item_package = OrderItemPackage.objects.filter(
            order_item__id=order_item.id
        )
        product_alias = ProductAlias.objects.filter(
            merchant_sku=order_item.merchant_sku,
            retailer_id=order_item.order.batch.retailer_id
        ).first()
        if not product_alias:
            return {
                "status": 400,
                "message": "Not found valid product alias",
            }
        check_qty_order = 0
        for order_item_package in list_ord_item_package:
            check_qty_order += order_item_package.quantity
        remain = abs(qty_order - check_qty_order)
        if quantity <= remain and quantity != 0:
            new_order_package = OrderPackage(
                box_id=box.id,
                order_id=order_item.id,
                length=box.length,
                width=box.width,
                height=box.height,
                dimension_unit=box.dimension_unit,
                weight=product_alias.product.weight * quantity,
                weight_unit=product_alias.product.weight_unit,
            )
            new_order_package.save()
            new_order_item_package = OrderItemPackage(
                quantity=quantity,
                package_id=new_order_package.id,
                order_item_id=order_item.id,
            )
            new_order_item_package.save()
            return {"status": 200, "message": "Create success"}

        return (
            {"status": 400, "message": "Order item is max quantity"}
            if remain == 0
            else {"status": 400, "message": f"Order item only need {remain}"}
        )

    except Exception as error:
        raise error


def delete_order_package_service(order_id_package: int):
    try:
        order_package = OrderPackage.objects.filter(id=order_id_package).first()
        if not order_package:
            raise ParseError("Order package id not exist!")

        list_order_package_item = OrderItemPackage.objects.filter(
            package__id=order_package.id
        )
        for order_item_package in list_order_package_item:
            order_item_package.delete()
        order_package.delete()

        return "delete success"

    except Exception as error:
        raise error
