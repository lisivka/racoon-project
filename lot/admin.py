from django.contrib import admin

from lot.models import VehicleModel, ColorModel, EngineModel, FuelModel, ConditionModel, \
    BrandModel, ModelModel, LotModel, PhotoModel

admin.site.register(VehicleModel)
admin.site.register(ColorModel)
admin.site.register(EngineModel)
admin.site.register(FuelModel)
admin.site.register(ConditionModel)
admin.site.register(BrandModel)
admin.site.register(ModelModel)
admin.site.register(LotModel)
admin.site.register(PhotoModel)
