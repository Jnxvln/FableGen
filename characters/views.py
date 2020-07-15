from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Character

# Create your views here.
class CharacterList(SuccessMessageMixin, ListView):
  model = Character
  context_object_name = 'characters'

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterDetail(DetailView):
  model = Character

class CharacterDelete(DeleteView):
    model = Character
    success_message = 'Character deleted successfully!'
    success_url = reverse_lazy('characters:character-list')

    def delete(self, request, *args, **kwargs):
      messages.success(self.request, self.success_message)
      return super(CharacterDelete, self).delete(request, *args, **kwargs)