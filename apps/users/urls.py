from django.urls import path


from .views import (
    UserListView,
    UserProfileUpdateView,
)
from . import views

urlpatterns = [
    path('', view=views.user_details, name='user_details'),
    path('<int:user_id>/', view=views.user_details, name='user_details'),
    path('sign_up/', view=views.sign_up, name='sign_up'),
    path('sign_up/<int:user_id>/', view=views.sign_up, name='sign_up'),
    path('sign_in/', view=views.sign_in, name='sign_in'),
    path('sign_out/', view=views.sign_out, name='sign_out'),
    path('password_reset/', view=views.password_reset, name='password_reset'),


    # path('', UserListView.as_view(), name='user-list'),
    path('/profile', UserProfileUpdateView.as_view(), name='users_profile_update'),
]
