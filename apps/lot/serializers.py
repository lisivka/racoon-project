from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserSerializer

from .models import (Color, Lot, Vehicle,
                     Engine, Fuel, Condition,
                     Brand, Model, Photo)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    class Meta:
        model = Model
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class LotSerializer(ModelSerializer):
    # color = serializers.StringRelatedField()
    color = ColorSerializer()
    owner = UserSerializer()
    vehicle = VehicleSerializers()
    engine = EngineSerializer()
    fuel = FuelSerializer()
    model = ModelSerializer()
    condition = ConditionSerializer()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Lot
        fields = '__all__'
