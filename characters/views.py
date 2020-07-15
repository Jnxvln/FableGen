from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Character

# Create your views here.
class CharacterList(ListView):
  model = Character
  context_object_name = 'characters'

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterDetail(DetailView):
  model = Character

