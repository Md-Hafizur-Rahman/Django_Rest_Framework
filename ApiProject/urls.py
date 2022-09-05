from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ApiApp.views import homeView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView),
    path('api/firstapp/', include('ApiApp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login-api',obtain_auth_token)
    
    ]
urlpatterns+=static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,Document_root=settings.STATIC_ROOT)

