from django.urls import path

from bid import consumers

websocket_urlpatterns = [
    path('ws/auctions/<int:auction_pk>/', consumers.AuctionBidConsumer.as_asgi()),
]
