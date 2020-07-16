from django.contrib import admin
from django.urls import path
from .views import QuestList, QuestCreate, QuestDetail, QuestUpdate, QuestDelete

app_name = 'quests'

urlpatterns = [
    path('', QuestList.as_view(), name='quest-list'),
    path('new/', QuestCreate.as_view(), name='quest-create'),
    path('<int:pk>/', QuestDetail.as_view(), name='quest-detail'),
    path('<int:pk>/update/', QuestUpdate.as_view(), name='quest-update'),
    path('<int:pk>/delete/', QuestDelete.as_view(), name='quest-delete'),
]
