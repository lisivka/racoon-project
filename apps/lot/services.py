from .models import LotModel, ColorModel, EngineModel, FuelModel, ConditionModel

class LotServices:

    def get_all(self):
        return LotModel.objects.all()

    def get_by_id(self, pk):
        return LotModel.objects.get(id=pk)

    def get_active(self):
        return LotModel.objects.filter(is_active=True)

