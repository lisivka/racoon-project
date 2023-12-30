from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.auction.models import Auction
from apps.auction.serializers import AuctionsSerializers


class AuctionsView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = AuctionsSerializers
    permission_classes = (IsAuthenticated,)
    queryset = Auction.objects.all()

    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)


class AuctionViewSet(ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionsSerializers