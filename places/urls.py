from django.contrib import admin
from django.urls import path
from .views import PlaceList, PlaceCreate, PlaceDetail, PlaceUpdate, PlaceDelete

app_name = 'places'

urlpatterns = [
    path('', PlaceList.as_view(), name='place-list'),
    path('new/', PlaceCreate.as_view(), name='place-create'),
    path('<int:pk>/', PlaceDetail.as_view(), name='place-detail'),
    path('<int:pk>/update', PlaceUpdate.as_view(), name='place-update'),
    path('<int:pk>/delete/', PlaceDelete.as_view(), name='place-delete'),
]
