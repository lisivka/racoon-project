from django.urls import path
from .views import LotListsView, LotView

urlpatterns = [
    path("", view=LotListsView.as_view(), name="lot_list"),
    path("", view=LotListsView.as_view(), name="lot_create"),
    path("/<int:pk>", view=LotView.as_view(), name="lot_delete"),
    path("/<int:pk>", view=LotView.as_view(), name="lot_update"),
    path("/<int:pk>", view=LotView.as_view(), name="lot_details"),
]
