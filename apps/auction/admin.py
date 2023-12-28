from django.contrib import admin

from .models import AuctionsModel
from django.core.serializers import serialize
from apps.bid.models import Bid


@admin.action(description="Mark selected as NOT active")
def make_not_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Mark selected as active")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


class BidInline(admin.TabularInline):
    model = Bid
    extra = 0


@admin.register(AuctionsModel)
class AuctionsAdmin(admin.ModelAdmin):
    """Admin configuration for the AuctionsModel."""
    inlines = [BidInline, ]
    verbose_name_plural = "Auctions"
    list_display = ('id', 'lot', 'is_active', 'start_date', 'end_date')
    list_display_links = ('id', 'lot', 'start_date', 'end_date')
    list_editable = ('is_active',)
    search_fields = ('lot', 'is_active')
    list_filter = ['is_active', ]

    actions = [make_active,
               make_not_active,
               ]
