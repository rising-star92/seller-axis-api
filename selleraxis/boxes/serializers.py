from rest_framework import serializers

from .models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def validate(self, data):
        if self.context["view"].request.headers.get("organization", None) != str(
            data["package_rule"].organization.id
        ):
            raise serializers.ValidationError("Package rules must be in organization")

        if self.context["view"].request.headers.get("organization", None) != str(
            data["barcode_size"].organization.id
        ):
            raise serializers.ValidationError("Barcode size must be in organization")

        return data
