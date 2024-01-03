from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserSerializer

from .models import Color, Lot, Vehicle, Engine, Fuel, Condition


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class EngineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class FuelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'


class LotSerializers(ModelSerializer):
    color = serializers.StringRelatedField()
    # color = ColorSerializer()
    owner = UserSerializer()
    vehicle = VehicleSerializers()
    engine = EngineSerializers()
    fuel = FuelSerializers()

    #

    class Meta:
        model = Lot
        fields = '__all__'
