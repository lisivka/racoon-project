from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Lot, Color, Vehicle, Engine, Fuel, Condition, Model, Brand, Photo
from .serializers import (ColorSerializer, LotSerializer, VehicleSerializers,
                          EngineSerializer, FuelSerializer, ConditionSerializer,
                          BrandSerializer, ModelSerializer, PhotoSerializer)
from common.views import get_offset_limit_page


class LotViewSet(ModelViewSet):
    serializer_class = LotSerializer
    queryset = Lot.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            # Дозволити всім користувачам перегляду (GET)
            return [AllowAny()]

        # Дозволити тільки аутентифікованим користувачам інші методи (POST, PUT, DELETE, тощо)
        return [IsAuthenticated()]


class ColorViewSet(ModelViewSet):
    serializer_class = ColorSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Color.objects.all()


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializers
    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all()

class EngineViewSet(ModelViewSet):
    serializer_class = EngineSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Engine.objects.all()

class FuelViewSet(ModelViewSet):
    serializer_class = FuelSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Fuel.objects.all()

class ConditionViewSet(ModelViewSet):
    serializer_class = ConditionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Condition.objects.all()

class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Brand.objects.all()

class ModelViewSet(ModelViewSet):
    serializer_class = ModelSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Model.objects.all()

class PhotoViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Photo.objects.all()


def lot_list(request, page=1):
    context = {}
    context["title"] = "Lots"
    offset, limit, page, page_prev, page_next = get_offset_limit_page(page)
    lots = Lot().get_all()
    context["lots"] = lots[offset:offset + limit]
    context["page"] = page
    context["page_next"] = page_next
    context["page_prev"] = page_prev

    return render(request, "lot/lots.html", context=context)


def lot_details(request, pk):
    lot = Lot().get_by_id(pk)
    photos = Photo.objects.all().filter(lot=lot)
    context = {}
    context["title"] = "Lot Details"
    context["lot"] = lot
    context["photos"] = photos

    return render(request, "lot/lot_details.html", context=context)
