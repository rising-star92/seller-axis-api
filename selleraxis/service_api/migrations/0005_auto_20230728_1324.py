# Generated by Django 3.2.14 on 2023-07-28 13:24

from django.db import migrations

from selleraxis.service_api.models import ServiceAPI, ServiceAPIAction
from selleraxis.services.models import Services


def create_default_fedex_shipping_api(apps, schema_editor):
    service = Services.objects.filter(name="FEDEX").first()

    fedex_shipping_sandbox_url = "https://apis-sandbox.fedex.com/ship/v1/shipments"

    fedex_shipping_production_url = "https://apis.fedex.com/ship/v1/shipments"

    fedex_shipping_method = "POST"

    fedex_shipping_header = """{
        "Authorization": "Bearer {{access_token}}",
        "Content-Type": "application/json",
        "x-locale": "en_US"
    }"""

    fedex_shipping_body = """{
        "labelResponseOptions": "URL_ONLY",
        "requestedShipment": {
            "shipper": {
                "address": {
                    "streetLines": [
                        "{{carrier.shipper.address}}"
                    ],
                    "city": "{{carrier.shipper.city}}",
                    "stateOrProvinceCode": "{{carrier.shipper.state}}",
                    "postalCode": "{{carrier.shipper.postal_code}}",
                    "countryCode": "{{carrier.shipper.country}}"
                },
                "contact": {
                    "personName": "{{carrier.shipper.name}}",
                    "emailAddress": "{{carrier.shipper.email}}",
                    "phoneNumber": "{{carrier.shipper.phone}}",
                    "companyName": "{{carrier.shipper.company}}"
                },
                "tins": [{"number": "", "tinType": "BUSINESS_UNION", "usage": ""}]
            },
            "recipients": [
                {
                    "contact": {
                        "personName": "{{verified_ship_to.name}}",
                        "emailAddress": "{{verified_ship_to.email}}",
                        "phoneNumber": "{{verified_ship_to.day_phone}}",
                        "companyName": "{{verified_ship_to.name}}"
                    },
                    "address": {
                        "streetLines": [
                            "{{verified_ship_to.address_1}}",
                            "{{verified_ship_to.address_2}}"
                        ],
                        "city": "{{verified_ship_to.city}}",
                        "stateOrProvinceCode": "{{verified_ship_to.state}}",
                        "postalCode": "{{verified_ship_to.postal_code}}",
                        "countryCode": "{{verified_ship_to.country}}"
                    }
                }
            ],
            "labelSpecification": {
                "imageType": "PNG",
                "labelStockType": "PAPER_4X6"
            },
            "shipDatestamp": "{{(datetime.date.today() + datetime.timedelta(days=5)).strftime("%Y-%m-%d")}}",
            "serviceType": "{{shipping_service}}",
            "packagingType": "YOUR_PACKAGING",
            "pickupType": "USE_SCHEDULED_PICKUP",
            "blockInsightVisibility": false,
            "edtRequestType": "NONE",
            "shippingChargesPayment": {
                "paymentType": "THIRD_PARTY",
                "payor": {
                    "responsibleParty": {
                        "address": {
                            "streetLines": ["10 FedEx Parkway", "Suite 302"],
                            "city": "Beverly Hills",
                            "stateOrProvinceCode": "CA",
                            "postalCode": "90210",
                            "countryCode": "US",
                            "residential": false
                        },
                        "accountNumber": {
                            "value": "{{carrier.account_number}}"
                        }
                    }
                }
            },
            "totalPackageCount": "{{order_packages | length}}",
            "requestedPackageLineItems": [
                {% for package in order_packages %}
                    {
                        "sequenceNumber": "{{loop.index}}",
                        "weight": {
                            "units": {% if package.weight_unit.upper() in ["LB", "LBS"] %}
                                "LB"
                            {% else %}
                                "{{package.weight_unit.upper()}}"
                            {% endif %},
                            "value": {{package.weight}}
                        },
                        "customerReferences": [
                            {
                                "customerReferenceType": "CUSTOMER_REFERENCE",
                                "value": "{{ref1}}"
                            },
                            {
                                "customerReferenceType": "P_O_NUMBER",
                                "value": "{{ref2}}"
                            },
                            {
                                "customerReferenceType": "INVOICE_NUMBER",
                                "value": "{{ref3}}"
                            },
                            {
                                "customerReferenceType": "DEPARTMENT_NUMBER",
                                "value": "{{ref4}}"
                            }
                        ],
                        "dimensions": {
                            "length": {{package.length}},
                            "width": {{package.width}},
                            "height": {{package.height}},
                            "units": "{{package.dimension_unit}}"
                        }
                    }{% if loop.index != order_packages | length %},{% endif %}
                {% endfor %}
            ]
        },
        "accountNumber": {"value": "{{carrier.account_number}}"},
        "shipAction": "CONFIRM",
        "processingOptionType": "SYNCHRONOUS_ONLY",
        "oneLabelAtATime": false
    }"""

    fedex_shipping_response = """{
        "shipments": {
            "type": "list",
            "field": "{{output.transactionShipments.0.pieceResponses}}",
            "data": {
                "tracking_number": "{{trackingNumber}}",
                "package_document": "{{packageDocuments.0.url}}"
            }
        }
    }"""

    ServiceAPI(
        action=ServiceAPIAction.SHIPPING,
        sandbox_url=fedex_shipping_sandbox_url,
        production_url=fedex_shipping_production_url,
        method=fedex_shipping_method,
        body=fedex_shipping_body,
        response=fedex_shipping_response,
        header=fedex_shipping_header,
        service=service,
    ).save()


class Migration(migrations.Migration):
    dependencies = [
        ("service_api", "0004_auto_20230728_0344"),
    ]

    operations = [migrations.RunPython(create_default_fedex_shipping_api)]
