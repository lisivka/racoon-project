from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from .services import LotServices

from .models import LotModel

def get_offset_limit_page(page):
    page_prev = page - 1
    page_next = page + 1
    if page <= 1:
        page = 1
        page_prev = 1
    LIMIT = 20
    OFFSET = page * LIMIT - LIMIT
    return OFFSET, LIMIT, page, page_prev, page_next

def lot_list(request, page=1):
    context = {}
    context["title"] = "Lots"
    offset, limit, page, page_prev, page_next = get_offset_limit_page(page)
    lots = LotServices().get_all()
    context["lots"] = lots[offset:offset + limit]
    context["page"] = page
    context["page_next"] = page_next
    context["page_prev"] = page_prev

    return render(request, "lot/lots.html", context=context)


def lot_details(request, pk):

    lot = LotServices().get_by_id(pk)
    context = {}
    context["title"] = "Lot Details"
    context["lot"] = lot

    return render(request, "lot/lot_details.html", context=context)