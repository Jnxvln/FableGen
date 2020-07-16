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

class CharacterUpdate(SuccessMessageMixin, UpdateView):
  model = Character
  fields = '__all__'
  success_message = '%(name)s updated successfully!'

class CharacterDelete(SuccessMessageMixin, DeleteView):
    model = Character
    success_message = '{character} deleted successfully!'
    success_url = reverse_lazy('characters:character-list')

    def delete(self, request, *args, **kwargs):
      character = Character.objects.get(pk=kwargs.get('pk'))
      self.success_message = f'{character} deleted successfully!'
      messages.success(self.request, self.success_message)
      return super(CharacterDelete, self).delete(request, *args, **kwargs)