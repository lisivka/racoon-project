from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Color, Lot, Photo, Vehicle
from .serializers import ColorSerializers, LotSerializers, VehicleSerializers
from common.views import get_offset_limit_page

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