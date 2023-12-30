from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Color, Lot, Photo, Vehicle
from .serializers import ColorSerializers, LotSerializers, VehicleSerializers
from .services import LotServices


class LotViewSet(ModelViewSet):
    serializer_class = LotSerializers
    permission_classes = (IsAuthenticated,)
    queryset = Lot.objects.all()

class ColorViewSet(ModelViewSet):
    serializer_class = ColorSerializers
    permission_classes = (IsAuthenticated,)
    queryset = Color.objects.all()

class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializers
    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all()


def get_offset_limit_page(page):
    page_prev = page - 1
    page_next = page + 1
    if page <= 1:
        page = 1
        page_prev = 1
    LIMIT = 20
    OFFSET = page * LIMIT - LIMIT
    return OFFSET, LIMIT, page, page_prev, page_next


def lot_list(request, page=1):
    context = {}
    context["title"] = "Lots"
    offset, limit, page, page_prev, page_next = get_offset_limit_page(page)
    lots = LotServices().get_all()
    context["lots"] = lots[offset:offset + limit]
    context["page"] = page
    context["page_next"] = page_next
    context["page_prev"] = page_prev

    return render(request, "lot/lots.html", context=context)


def lot_details(request, pk):

    lot = LotServices().get_by_id(pk)
    photos = Photo.objects.all().filter(lot=lot)
    context = {}
    context["title"] = "Lot Details"
    context["lot"] = lot
    context["photos"] = photos

    return render(request, "lot/lot_details.html", context=context)