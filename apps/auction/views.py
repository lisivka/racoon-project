from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from apps.auction.models import Auction
from apps.auction.serializers import AuctionsSerializer
from common.views import get_offset_limit_page
from apps.lot.models import Photo
from apps.bid.models import Bid



class AuctionsView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = AuctionsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Auction.objects.all()

    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)


class AuctionViewSet(ModelViewSet):
    queryset = Auction().get_all()
    serializer_class = AuctionsSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            # Дозволити всім користувачам перегляду (GET)
            return [AllowAny()]

        # Дозволити тільки аутентифікованим користувачам інші методи (POST, PUT, DELETE, тощо)
        return [IsAuthenticated()]

def auction_list(request, page=1):
    context = {}
    context["title"] = "Auctions"
    offset, limit, page, page_prev, page_next = get_offset_limit_page(page)
    auctions = Auction().get_limit(offset, limit)
    for auction in auctions:
        #Get the first photo for each lot
        photo = Photo.objects.filter(lot=auction.lot).first()
        if photo:
            auction.photo_url = photo.url
        else:
            auction.photo_url = None
        #Get the last bid for each auction
        bid = Bid().get_by_auction(auction.id).first()
        if bid:
            auction.last_bid = bid.bet
        else:
            auction.last_bid = "-"

    context["auctions"] = auctions
    context["page"] = page
    context["page_next"] = page_next
    context["page_prev"] = page_prev

    return render(request, "auction/auctions.html", context=context)



def auction_details(request, pk):
    auction = Auction().get_by_id(pk)
    lot = auction.lot
    photos = Photo.objects.all().filter(lot=auction.lot)
    bids = Bid().get_by_auction(pk)

    context = {}
    context["title"] = "Auction Details"
    context["auction"] = auction
    context["lot"] = lot
    context["photos"] = photos
    context["bids"] = bids

    return render(request, "auction/auction_details.html", context=context)

