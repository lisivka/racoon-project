from django.urls import path

from .views import (
    AuctionsView,
)
from . import views

urlpatterns = [
# <<<<<<< add-html-and-API-pages
#     path('', views.auction_list, name='auction_list'),
    path('/page=<int:page>/', views.auction_list, name='auction_list'),
#     path('/<int:pk>', views.auction_details, name='auction_details'),
    # path('', AuctionsView.as_view(), name='auction_list'),
    # path('<int:pk>/', AuctionsView.as_view(), name='auction_detail'),

# =======
    path('', AuctionsView.as_view(), name='auction-list'),
    path('<int:pk>/', AuctionsView.as_view(), name='auction-detail'),
# >>>>>>> add_djoser_for_user
]
