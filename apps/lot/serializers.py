from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserSerializer

from .models import Color, Lot, Vehicle


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class LotSerializers(ModelSerializer):
    color = serializers.StringRelatedField()
    # color = ColorSerializer()
    owner = UserSerializer()

    class Meta:
        model = Lot
        fields = '__all__'
