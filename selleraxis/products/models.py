from django.db import models

from selleraxis.core.base_model import SQSSyncModel
from selleraxis.product_series.models import ProductSeries


class Product(SQSSyncModel):
    WEIGHT_UNIT = (("LB", "lb"), ("LBS", "lbs"), ("KG", "kg"))
    sku = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=100)
    available = models.CharField(max_length=100)
    upc = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    unit_cost = models.FloatField()
    qty_on_hand = models.IntegerField()
    qty_pending = models.IntegerField(default=0)
    qty_reserve = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    weight = models.FloatField(default=0)
    weight_unit = models.CharField(max_length=255, choices=WEIGHT_UNIT, default="lb")
    volume = models.FloatField(default=0)
    volume_unit = models.CharField(max_length=255, blank=True, default="")
    qbo_product_id = models.IntegerField(blank=True, null=True)
    product_series = models.ForeignKey(
        ProductSeries,
        on_delete=models.CASCADE,
        null=True,
        related_name="products",
    )
    sync_token = models.IntegerField(null=True)
    inv_start_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    qbo_account_ref_name = models.CharField(
        max_length=255, blank=True, default="Inventory Asset"
    )
    qbo_account_ref_id = models.IntegerField(null=True)
    income_account_ref_name = models.CharField(
        max_length=255, blank=True, default="Sales of Product Income"
    )
    income_account_ref_id = models.IntegerField(null=True)
    expense_account_ref_name = models.CharField(
        max_length=255, blank=True, default="Cost of Goods Sold"
    )
    expense_account_ref_id = models.IntegerField(null=True)
