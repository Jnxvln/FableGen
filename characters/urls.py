from django.contrib import admin
from django.urls import path
from .views import CharacterList, CharacterCreate, CharacterDetail

app_name = 'characters'

urlpatterns = [
    path('', CharacterList.as_view(), name='character-list'),
    path('new/', CharacterCreate.as_view(), name='character-create'),
    path('<int:pk>/', CharacterDetail.as_view(), name='character-detail'),
]
