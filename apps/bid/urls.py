from django.urls import path

from .views import BidViewSet

urlpatterns = [
    path(
        '<int:auction_pk>/bids/',
        BidViewSet.as_view({'get': 'list'}),
        name='bid-list',
    )
]
