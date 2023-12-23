from django.contrib import admin

from .models import AuctionsModel


@admin.register(AuctionsModel)
class AuctionsAdmin(admin.ModelAdmin):
    """Admin configuration for the AuctionsModel."""

    verbose_name_plural = "Auctions"
    list_display = ('lot', 'is_active', 'start_date', 'end_date')
    search_fields = ('lot', 'is_active')
