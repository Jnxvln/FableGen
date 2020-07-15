from django.contrib import admin
from django.urls import path
from .views import PlaceList, PlaceCreate, PlaceDetail, PlaceDelete

app_name = 'places'

urlpatterns = [
    path('', PlaceList.as_view(), name='place-list'),
    path('new/', PlaceCreate.as_view(), name='place-create'),
    path('<int:pk>/', PlaceDetail.as_view(), name='place-detail'),
    path('delete/<int:pk>/', PlaceDelete.as_view(), name='place-delete'),
]
