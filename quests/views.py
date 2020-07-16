from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Quest

class QuestList(ListView):
  model = Quest
  context_object_name = 'quests'

class QuestCreate(CreateView):
  model = Quest
  fields = '__all__'

class QuestDetail(DetailView):
  model = Quest

class QuestUpdate(SuccessMessageMixin, UpdateView):
  model = Quest
  fields = '__all__'
  success_message = '%(name)s updated successfully!'

class QuestDelete(DeleteView):
  model = Quest
  success_message = '{quest} deleted successfully!'
  success_url = reverse_lazy('quests:quest-list')

  def delete(self, request, *args, **kwargs):
    quest = Quest.objects.get(pk=kwargs.get('pk'))
    self.success_message = f'{quest} deleted successfully!'
    messages.success(self.request, self.success_message)
    return super(QuestDelete, self).delete(request, *args, **kwargs)