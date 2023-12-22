from django.urls import path

from .views import (
    AuctionsView,
)

urlpatterns = [
    path('', AuctionsView.as_view(), name='auction-list'),

]
