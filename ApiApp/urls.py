from django.urls import path,include

from ApiApp import views
from .views import *
urlpatterns = [
    #path('', views.HomeView.as_view(), name='home'),
   # path('api/',views.HomeApiView.as_view(),name='api'),
    path('first/',firstApi),
    path('registration/',registrationApi),
    path('contact/',ContactApiView.as_view()),
    path('post/',PostCreateView.as_view()),
    # path('post/<int:id>/',POSTRetriviewAPIView.as_view()),
    path('post/<int:id>/',POSTretrieveupdateAPIView.as_view()),
    # path('postlist/',POSTListAPIView.as_view()),
]