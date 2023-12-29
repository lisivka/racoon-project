from .models import Lot


class LotServices:

    def get_all(self):
        return Lot.objects.all()

    def get_by_id(self, pk):
        return Lot.objects.get(id=pk)

    def get_active(self):
        return Lot.objects.filter(is_active=True)

