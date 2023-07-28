from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('places',PlaceViewSet)


urlpatterns = [ 
     path('', include(router.urls)),

]