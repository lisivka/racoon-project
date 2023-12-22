from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path("", view=views.index, name="home"),

    path('auth', include('apps.auth.urls')),
    path('users', include('apps.users.urls')),
    path('auctions', include('apps.auction.urls')),
]

# Include URL patterns for API documentation
urlpatterns += doc_urls
