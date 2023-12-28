from django.shortcuts import render
from .services import LotServices
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import LotSerializer, PhotoSerializer
from .models import LotModel, PhotoModel


class LotListsView(ListCreateAPIView):
    queryset = LotServices().get_all()
    serializer_class = LotSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = LotSerializer(queryset, many=True)
        return render(request, "lot/lots.html", {"lot_list": serializer.data})


class LotView(RetrieveUpdateDestroyAPIView):
    queryset = LotServices().get_all()
    serializer_class = LotSerializer
    # permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk):
        lot = LotServices().get_by_id(pk)
        photo = PhotoModel.objects.get(lot_id=lot.id)
        lot_serializer = LotSerializer(lot)
        photo_serializer = PhotoSerializer(photo)
        return render(
            request,
            "lot/lot_details.html",
            {
                "lot": lot_serializer.data,
                "photo": photo_serializer.data
            })


# def get_offset_limit_page(page):
#     page_prev = page - 1
#     page_next = page + 1
#     if page <= 1:
#         page = 1
#         page_prev = 1
#     LIMIT = 20
#     OFFSET = page * LIMIT - LIMIT
#     return OFFSET, LIMIT, page, page_prev, page_next
