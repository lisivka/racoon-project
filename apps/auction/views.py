from rest_framework.generics import ListCreateAPIView

from apps.auction.models import AuctionsModel
from apps.auction.serializers import AuctionsSerializers


class AuctionsView(ListCreateAPIView):
    queryset = AuctionsModel
    serializer_class = AuctionsSerializers
