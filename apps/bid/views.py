from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, viewsets
from rest_framework.exceptions import NotFound

from .models import Bid
from .serializers import BidSerializer


class BidViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = BidSerializer
    ordering = ('-created_at', )

    def get_queryset(self):
        auction_id = self.kwargs.get('auction_pk', None)
        if auction_id is None:
            raise NotFound({'message': _('Auction not found.')})

        queryset = Bid.objects.filter(auction_id=auction_id)

        queryset = queryset.order_by(*self.ordering)

        return queryset
