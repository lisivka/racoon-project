from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.show_lots, name="lot-list"),
    path("/<int:pk>", view=views.lot_detail, name="lot-detail"),
]
