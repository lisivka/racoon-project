from django.contrib import admin

from .models import Bid


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    """Admin configuration for the Bid model."""

    list_display = ('id', 'user', 'auction', 'bet')
    list_display_links = ('id', 'user', 'auction', 'bet')
