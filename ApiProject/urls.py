from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from ApiApp.views import homeView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenObtainPairView
from rest_framework.authentication import TokenAuthentication
urlpatterns = [
    path("admin/", admin.site.urls),
    #path("", homeView),
    path('api/firstapp/', include('ApiApp.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/login-api',obtain_auth_token),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
urlpatterns+=static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,Document_root=settings.STATIC_ROOT)

