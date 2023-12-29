from django.contrib import admin

from apps.bid.models import Bid

from .models import Auction


@admin.action(description="Mark selected as NOT active")
def make_not_active(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Mark selected as active")
def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


class BidInline(admin.TabularInline):
    model = Bid
    extra = 0


@admin.register(Auction)
class AuctionsAdmin(admin.ModelAdmin):
    """Admin configuration for the AuctionsModel."""
    inlines = (BidInline, )
    verbose_name_plural = 'Auctions'
    list_display = ('id', 'lot', 'status', 'start_date', 'end_date')
    list_display_links = ('id', 'lot', 'start_date', 'end_date')
    list_editable = ('status',)
    search_fields = ('lot', 'status')
    list_filter = ('status', )

    actions = (make_active, make_not_active)
