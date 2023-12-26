from django.template import loader
from django.http.response import HttpResponse

from .models import LotModel


def show_lots(request):
    tmpl = loader.get_template("lots.html")
    lots = LotModel.objects.all()
    content = {
        "lot_list": lots
    }
    return HttpResponse(tmpl.render(content, request))


def lot_detail(request, pk):
    tmpl = loader.get_template("lot_info.html")
    lot = LotModel.objects.get(id=pk)
    content = {
        "lot_detail": lot
    }
    return HttpResponse(tmpl.render(content, request))
