from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.index, name='home'),

    path('v1/auth', include('apps.auth.urls')),
    path('v1/users', include('apps.users.urls')),
    path('v1/auctions', include('apps.auction.urls')),
    path('v1/lots', include('apps.lot.urls')),
    path('v1/auctions/', include('apps.bid.urls')),
]

# Include URL patterns for API documentation
urlpatterns += doc_urls
