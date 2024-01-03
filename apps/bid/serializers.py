from pydantic import ValidationError
from rest_framework import serializers

from apps.users.serializers import UserSerializer

from .models import Bid
from .schemas import BidSchema


class BidSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Bid
        fields = '__all__'

    def validate(self, data):
        try:
            BidSchema.model_validate(data)
        except ValidationError as error:
            raise serializers.ValidationError(error) from error
