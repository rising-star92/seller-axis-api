from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from selleraxis.core.pagination import Pagination
from selleraxis.core.permissions import check_permission
from selleraxis.core.views import BulkUpdateAPIView
from selleraxis.permissions.models import Permissions
from selleraxis.product_warehouse_static_data.services import (
    send_all_retailer_id_sqs,
    send_retailer_id_sqs,
)

from .models import ProductWarehouseStaticData
from .serializers import (
    BulkProductWarehouseStaticDataSerializer,
    ProductWarehouseStaticDataSerializer,
)


class ListCreateProductWarehouseStaticDataView(ListCreateAPIView):
    model = ProductWarehouseStaticData
    serializer_class = ProductWarehouseStaticDataSerializer
    queryset = ProductWarehouseStaticData.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination

    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["status", "created_at"]
    search_fields = ["status"]

    def check_permissions(self, _):
        match self.request.method:
            case "GET":
                return check_permission(
                    self, Permissions.READ_PRODUCT_WAREHOUSE_STATIC_DATA
                )
            case _:
                return check_permission(
                    self, Permissions.CREATE_PRODUCT_WAREHOUSE_STATIC_DATA
                )


class UpdateDeleteProductWarehouseStaticDataView(RetrieveUpdateDestroyAPIView):
    model = ProductWarehouseStaticData
    serializer_class = ProductWarehouseStaticDataSerializer
    lookup_field = "id"
    queryset = ProductWarehouseStaticData.objects.all()
    permission_classes = [IsAuthenticated]

    def check_permissions(self, _):
        match self.request.method:
            case "GET":
                return check_permission(
                    self, Permissions.READ_PRODUCT_WAREHOUSE_STATIC_DATA
                )
            case "DELETE":
                return check_permission(
                    self, Permissions.DELETE_PRODUCT_WAREHOUSE_STATIC_DATA
                )
            case _:
                return check_permission(
                    self, Permissions.UPDATE_PRODUCT_WAREHOUSE_STATIC_DATA
                )


class BulkUpdateDeleteProductWarehouseStaticDataView(BulkUpdateAPIView):
    queryset = ProductWarehouseStaticData.objects.all()
    serializer_class = BulkProductWarehouseStaticDataSerializer

    def check_permissions(self, _):
        match self.request.method:
            case "GET":
                return check_permission(
                    self, Permissions.READ_PRODUCT_WAREHOUSE_STATIC_DATA
                )
            case "DELETE":
                return check_permission(
                    self, Permissions.DELETE_PRODUCT_WAREHOUSE_STATIC_DATA
                )
            case _:
                return check_permission(
                    self, Permissions.UPDATE_PRODUCT_WAREHOUSE_STATIC_DATA
                )


####


class GetRetailerToUpdateInventoryView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "product_warehouse_static_ids",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
            ),
            # ... add more parameters as needed ...
        ]
    )
    def get(self, request):
        ids = request.query_params.get("product_warehouse_static_ids")
        if ids is not None:
            list_ids = ids.split(",")
            send_retailer_id_sqs(list_ids)
        else:
            send_all_retailer_id_sqs()
        return Response("done")
