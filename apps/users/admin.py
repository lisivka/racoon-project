from django.contrib import admin

from .models import UserModel, ProfileModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for the UserModel."""

    list_display = ['id','email', 'is_active', 'is_staff', 'is_superuser']
    list_display_links =  ['id','email']
    list_editable = ['is_active', 'is_staff']
    search_fields = ['email', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff', 'is_superuser']


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    """Admin configuration for the UserModel."""

    verbose_name_plural = "profile"
    list_display = ('name', 'surname', 'age')
    search_fields = ('name', 'surname')

