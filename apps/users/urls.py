from django.urls import path

from .views import (
    UserListView,
    UserProfileUpdateView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('/profile', UserProfileUpdateView.as_view(), name='users_profile_update'),

]
