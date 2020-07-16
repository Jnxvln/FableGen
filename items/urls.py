from django.contrib import admin
from django.urls import path
from .views import ItemList, ItemCreate, ItemDetail, ItemUpdate, ItemDelete

app_name = 'items'

urlpatterns = [
    path('', ItemList.as_view(), name='item-list'),
    path('new/', ItemCreate.as_view(), name='item-create'),
    path('<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('<int:pk>/update', ItemUpdate.as_view(), name='item-update'),
    path('<int:pk>/delete', ItemDelete.as_view(), name='item-delete'),
]
