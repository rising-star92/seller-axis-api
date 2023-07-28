from django.db import models

from selleraxis.organizations.models import Organization


class Retailer(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, default="")
    merchant_id = models.CharField(max_length=255, default="lowes")
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="retailer_organization"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
