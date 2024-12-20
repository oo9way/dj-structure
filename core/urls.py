from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from apps.users.views import message_handler
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('webhook/', csrf_exempt(message_handler)),
    path('admin/', admin.site.urls),
    path("api/v1/books/", include("apps.books.urls")),
    path("api/v1/users/", include("apps.users.urls")),
    path("swagger/", include("core.scheme")),
]


if settings.DEBUG:
    # /media --> media_root
    # /static --> static_root
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += debug_toolbar_urls()
