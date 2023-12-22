from django.contrib import admin

from .models import UserModel, ProfileModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for the UserModel."""

    list_display = ['email']


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for the UserModel."""

    verbose_name_plural = "profile"
    list_display = ('name', 'surname', 'age')
    search_fields = ('name', 'surname')

