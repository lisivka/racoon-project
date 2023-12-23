from django.contrib import admin

from .models import VehicleModel, ColorModel, EngineModel, FuelModel, ConditionModel
from .models import BrandModel, ModelModel, LotModel, PhotoModel

@admin.action(description="Mark selected as NOT active")
def make_not_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Mark selected as active")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


admin.site.register(VehicleModel)
admin.site.register(ColorModel)
admin.site.register(EngineModel)
admin.site.register(FuelModel)
admin.site.register(ConditionModel)
admin.site.register(BrandModel)
admin.site.register(ModelModel)
# admin.site.register(PhotoModel)

@admin.register(LotModel)
class LotAdmin(admin.ModelAdmin):
    """Admin configuration for the LotModel."""

    verbose_name_plural = "Lots"
    list_display = ('id', 'owner', 'vehicle', 'is_active', 'fuel', 'condition', 'state', 'color')
    list_display_links = ('id', 'owner', 'vehicle')
    list_editable = ('is_active',)
    search_fields = ('owner', 'vehicle', 'is_active' )
    list_filter = ('is_active','fuel', 'condition', 'state', 'color', 'vehicle')

    # @admin.action(description="Mark selected as NOT active")
    # def make_not_active(modeladmin, request, queryset):
    #     queryset.update(is_active=False)
    #
    # @admin.action(description="Mark selected as active")
    # def make_active(modeladmin, request, queryset):
    #     queryset.update(is_active=True)

    actions = [make_not_active,
               make_active,
               ]

@admin.register(PhotoModel)
class PhotoAdmin(admin.ModelAdmin):
    """Admin configuration for the PhotoModel."""

    verbose_name_plural = "Photos"
    list_display = ('id', 'lot', 'url')
    list_display_links = ('id', 'lot', 'url')
    search_fields = ('lot', 'photo')

