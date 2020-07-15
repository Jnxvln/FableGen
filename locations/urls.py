from django.contrib import admin
from django.urls import path
from .views import LocationList, LocationCreate, LocationDetail

app_name = 'locations'

urlpatterns = [
    path('', LocationList.as_view(), name='location-list'),
    path('new/', LocationCreate.as_view(), name='location-create'),
    path('<int:pk>/', LocationDetail.as_view(), name='location-detail'),
]
