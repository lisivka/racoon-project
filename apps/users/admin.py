from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """Admin configuration for the User model."""
    inlines = (ProfileInline,)
    list_display = ('id', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'email', 'is_active', 'is_superuser')
    search_fields = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for the Profile model."""

    verbose_name_plural = 'profile'
    list_display = ('name', 'surname')
    search_fields = ('name', 'surname')
