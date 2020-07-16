from django.contrib import admin
from django.urls import path
from .views import CharacterList, CharacterCreate, CharacterDetail, CharacterUpdate, CharacterDelete

app_name = 'characters'

urlpatterns = [
    path('', CharacterList.as_view(), name='character-list'),
    path('new/', CharacterCreate.as_view(), name='character-create'),
    path('<int:pk>/', CharacterDetail.as_view(), name='character-detail'),
    path('<int:pk>/update', CharacterUpdate.as_view(), name='character-update'),
    path('<int:pk>/delete/', CharacterDelete.as_view(), name='character-delete'),
]
