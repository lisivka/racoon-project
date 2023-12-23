from django.urls import path

from .views import (
    AuctionsView,
)

urlpatterns = [
    path('', AuctionsView.as_view(), name='auction-list'),
    path('/<int:pk>', AuctionsView.as_view(), name='auction-detail'),

]
