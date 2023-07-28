from django.db.models import Prefetch
from django.forms import model_to_dict
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from selleraxis.core.pagination import Pagination
from selleraxis.core.permissions import check_permission
from selleraxis.organizations.models import Organization
from selleraxis.permissions.models import Permissions
from selleraxis.retailer_person_places.models import RetailerPersonPlace
from selleraxis.retailer_purchase_orders.models import RetailerPurchaseOrder
from selleraxis.retailer_purchase_orders.serializers import (
    OrganizationPurchaseOrderCheckSerializer,
    OrganizationPurchaseOrderImportSerializer,
    ReadRetailerPurchaseOrderSerializer,
    RetailerPurchaseOrderSerializer,
)
from selleraxis.retailers.models import Retailer
from selleraxis.service_api.models import ServiceAPI, ServiceAPIAction
from selleraxis.services.models import Services

from .services.acknowledge_xml_handler import AcknowledgeXMLHandler
from .services.services import package_divide_service


class ListCreateRetailerPurchaseOrderView(ListCreateAPIView):
    model = RetailerPurchaseOrder
    queryset = RetailerPurchaseOrder.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    ordering_fields = ["retailer_purchase_order_id", "created_at"]
    search_fields = ["retailer_purchase_order_id"]
    filterset_fields = ["batch", "batch__retailer"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadRetailerPurchaseOrderSerializer
        else:
            return RetailerPurchaseOrderSerializer

    def get_queryset(self):
        return self.queryset.filter(
            batch__retailer__organization_id=self.request.headers.get("organization")
        )

    def check_permissions(self, _):
        match self.request.method:
            case "GET":
                return check_permission(self, Permissions.READ_RETAILER_PURCHASE_ORDER)
            case _:
                return check_permission(
                    self, Permissions.CREATE_RETAILER_PURCHASE_ORDER
                )


class UpdateDeleteRetailerPurchaseOrderView(RetrieveUpdateDestroyAPIView):
    model = RetailerPurchaseOrder
    lookup_field = "id"
    queryset = RetailerPurchaseOrder.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadRetailerPurchaseOrderSerializer
        else:
            return RetailerPurchaseOrderSerializer

    def get_queryset(self):
        return self.queryset.filter(
            batch__retailer__organization_id=self.request.headers.get("organization")
        )

    def check_permissions(self, _):
        match self.request.method:
            case "GET":
                return check_permission(self, Permissions.READ_RETAILER_PURCHASE_ORDER)
            case "DELETE":
                return check_permission(
                    self, Permissions.DELETE_RETAILER_PURCHASE_ORDER
                )
            case _:
                return check_permission(
                    self, Permissions.UPDATE_RETAILER_PURCHASE_ORDER
                )


class RetailerPurchaseOrderAcknowledgeCreateAPIView(CreateAPIView):
    queryset = RetailerPurchaseOrder.objects.all()
    serializer_class = ReadRetailerPurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(
            batch__retailer__organization_id=self.request.headers.get("organization")
        )

    def post(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = ReadRetailerPurchaseOrderSerializer(instance)
            ack_obj = AcknowledgeXMLHandler(data=serializer.data)
            file, file_created = ack_obj.upload_xml_file()
            if file_created:
                return Response(status=HTTP_204_NO_CONTENT)

        except RetailerPurchaseOrder.DoesNotExist:
            raise ValidationError("Purchase order does not exist.")

        except Exception:
            pass

        raise ValidationError("Could not create Acknowledge XML file to SFTP.")


class OrganizationPurchaseOrderRetrieveAPIView(RetrieveAPIView):
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.get_queryset().get()

    def get_queryset(self):
        organization_id = self.request.headers.get("organization")
        return self.queryset.filter(pk=organization_id).prefetch_related(
            Prefetch(
                "retailer_organization",
                queryset=Retailer.objects.prefetch_related(
                    "retailer_order_batch"
                ).select_related("retailer_commercehub_sftp"),
            )
        )


class OrganizationPurchaseOrderCheckView(OrganizationPurchaseOrderRetrieveAPIView):
    serializer_class = OrganizationPurchaseOrderCheckSerializer


class OrganizationPurchaseOrderImportView(OrganizationPurchaseOrderRetrieveAPIView):
    serializer_class = OrganizationPurchaseOrderImportSerializer


class PackageDivideView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(
            batch__retailer__organization_id=self.request.headers.get("organization")
        )

    def check_permissions(self, _):
        match self.request.method:
            case "POST":
                return check_permission(self, Permissions.PACKAGE_DIVIDE)

    def post(self, request, *args, **kwargs):
        response = package_divide_service(
            retailer_purchase_order_id=self.kwargs.get("id"),
        )
        return JsonResponse(
            {"message": "Successful!", "data": response},
            status=status.HTTP_200_OK,
        )


class ShipToAddressValidationView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = RetailerPurchaseOrder.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            batch__retailer__organization_id=self.request.headers.get("organization")
        )

    def post(self, request, pk, *args, **kwargs):
        order = get_object_or_404(self.get_queryset(), id=pk)

        service = Services.objects.filter(name="FEDEX").first()

        login_api = ServiceAPI.objects.filter(
            service_id=service.id, action=ServiceAPIAction.LOGIN
        ).first()

        try:
            login_response = login_api.request(
                {
                    "client_id": service.general_client_id,
                    "client_secret": service.general_client_secret,
                }
            )
        except KeyError:
            return Response(
                {"error": "Login to service fail!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        address_validation_data = model_to_dict(order.ship_to)
        address_validation_data["access_token"] = login_response["access_token"]

        address_validation_api = ServiceAPI.objects.filter(
            service_id=service.id, action=ServiceAPIAction.ADDRESS_VALIDATION
        ).first()

        try:
            address_validation_response = address_validation_api.request(
                address_validation_data
            )
        except KeyError:
            return Response(
                {"error": "Address validation fail!"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        verified_ship_to = RetailerPersonPlace(
            address_1=address_validation_response["address_1"],
            address_2=address_validation_response["address_2"],
            city=address_validation_response["city"],
            state=address_validation_response["state"],
            postal_code=address_validation_response["postal_code"],
            country=address_validation_response["country"],
            retailer_id=order.batch.retailer.id,
        )

        order.verified_ship_to = verified_ship_to
        verified_ship_to.save()
        order.save()

        return JsonResponse(
            {"message": "Successful!", "data": model_to_dict(verified_ship_to)},
            status=status.HTTP_200_OK,
        )
