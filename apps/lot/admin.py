from django.contrib import admin

from apps.auction.models import Auction

from .models import Brand, Color, Condition, Engine, Fuel, Lot, Model, Photo, Vehicle


@admin.action(description="Mark selected as NOT active")
def make_not_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Mark selected as active")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


admin.site.register(Vehicle)
admin.site.register(Color)
admin.site.register(Engine)
admin.site.register(Fuel)
admin.site.register(Condition)
admin.site.register(Brand)
admin.site.register(Model)
# admin.site.register(PhotoModel)


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


class AuctionInline(admin.StackedInline):
    model = Auction
    extra = 0


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    """Admin configuration for the Lot model."""
    inlines = (AuctionInline, PhotoInline)
    verbose_name_plural = 'Lots'
    list_display = ('id', 'owner', 'vehicle', 'is_active', 'fuel', 'condition', 'status', 'color')
    list_display_links = ('id', 'owner', 'vehicle')
    list_editable = ('is_active',)
    search_fields = ('owner', 'vehicle', 'is_active')
    list_filter = ('is_active', 'fuel', 'condition', 'status', 'color', 'vehicle')
    actions = (make_not_active, make_active)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Admin configuration for the Photo model."""

    verbose_name_plural = 'Photos'
    list_display = ('id', 'lot', 'url')
    list_display_links = ('id', 'lot', 'url')
    search_fields = ('lot', 'photo')
