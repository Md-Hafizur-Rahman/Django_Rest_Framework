from django.urls import path,include

from ApiApp import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('api/',views.HomeApiView.as_view(),name='api'),
]