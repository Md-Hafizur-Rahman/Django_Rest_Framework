from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ApiApp.views import homeView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView),
    path('api/firstapp/', include('ApiApp.urls')),
    path('api-auth/', include('rest_framework.urls'))
    
    ]
urlpatterns+=static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,Document_root=settings.STATIC_ROOT)

