from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", view=views.index, name="home")
]

# Include URL patterns for API documentation
urlpatterns += doc_urls
