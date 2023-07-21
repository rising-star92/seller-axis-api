from rest_framework.generics import RetrieveUpdateDestroyAPIView

from selleraxis.core.views import BaseGenericAPIView, BaseListCreateAPIView

from .models import ProductSeries
from .serializers import ProductSeriesSerializer, ReadProductSeriesSerializer


class ListCreateProductSeriesView(BaseListCreateAPIView):
    serializer_class = ProductSeriesSerializer
    queryset = ProductSeries.objects.all()
    search_fields = ["series"]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadProductSeriesSerializer
        return ProductSeriesSerializer

    def perform_create(self, serializer):
        serializer.save(organization_id=self.request.headers.get("organization"))

    def get_queryset(self):
        return self.queryset.filter(
            organization_id=self.request.headers.get("organization")
        )


class UpdateDeleteProductSeriesView(BaseGenericAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSeriesSerializer
    queryset = ProductSeries.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadProductSeriesSerializer
        return ProductSeriesSerializer
