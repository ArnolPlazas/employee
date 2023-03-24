from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('', include('applications.employees.urls')),
    path('', include('applications.departments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
