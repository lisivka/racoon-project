from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.lot_list, name="lot_list"),
    path("/page=<int:page>/", view=views.lot_list, name="lot_list"),
    path("/<int:pk>", view=views.lot_details, name="lot_details"),
]
