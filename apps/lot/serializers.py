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
    models = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Brand
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    brande = BrandSerializer()
    class Meta:
        model = Model
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class LotSerializer(serializers.ModelSerializer):
    # color = serializers.StringRelatedField()
    color = ColorSerializer(read_only=True)
    owner = UserSerializer(read_only=True)
    vehicle = VehicleSerializers(read_only=True)
    engine = EngineSerializer(read_only=True)
    fuel = FuelSerializer(read_only=True)
    model = ModelSerializer(read_only=True)
    condition = ConditionSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Lot
        fields = '__all__'
