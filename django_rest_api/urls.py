from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('supersecret/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Django Rest Api Admin"
admin.site.site_title = "Django Rest Api Admin Portal"
admin.site.index_title = "Welcome to the Django Rest Api Admin Portal"