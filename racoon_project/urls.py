from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.auction.views import AuctionViewSet
from apps.lot.views import ColorViewSet, LotViewSet, VehicleViewSet

from . import views
from .yasg import urlpatterns as doc_urls

router = DefaultRouter()
router.register(r'auctions', AuctionViewSet, basename="auctions")
router.register(r'lots', LotViewSet, basename="lots")
router.register(r'colors', ColorViewSet, basename="colors")
router.register(r'vehicles', VehicleViewSet, basename="vehicles")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('', view=views.index, name='home'),

    path('users/', include('apps.users.urls')),
    path('auctions/', include('apps.auction.urls')),
    path('lots/', include('apps.lot.urls')),
    path('auctions/', include('apps.bid.urls')),

    # for API
    path('api/v1/', include(router.urls)),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/auctions/', include('apps.bid.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include URL patterns for API documentation
urlpatterns += doc_urls
