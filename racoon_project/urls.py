from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('', view=views.index, name='home'),

    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/auctions/', include('apps.auction.urls')),
    path('api/v1/lots/', include('apps.lot.urls')),
    path('api/v1/auctions/', include('apps.bid.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include URL patterns for API documentation
urlpatterns += doc_urls
