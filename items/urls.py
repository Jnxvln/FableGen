from django.contrib import admin
from django.urls import path
from .views import ItemList, ItemCreate, ItemDetail, ItemDelete

app_name = 'items'

urlpatterns = [
    path('', ItemList.as_view(), name='item-list'),
    path('new/', ItemCreate.as_view(), name='item-create'),
    path('<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('delete/<int:pk>/', ItemDelete.as_view(), name='item-delete'),
]
