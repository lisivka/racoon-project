from django.urls import path

from .views import (
    AuctionsView,
)
from . import views

urlpatterns = [
    path('', views.auction_list, name='auction_list'),
    path('page=<int:page>/', views.auction_list, name='auction_list'),
    path('<int:pk>/', views.auction_details, name='auction_details'),

]
