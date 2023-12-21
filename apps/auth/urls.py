from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import AuthRegisterView, AuthMeView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/me', AuthMeView.as_view(), name='auth_me'),

    path('refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/register', AuthRegisterView.as_view(), name='auth_register')
]