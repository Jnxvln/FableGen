from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Item

# Create your views here.
class ItemList(SuccessMessageMixin, ListView):
  model = Item
  context_object_name = 'items'

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemDetail(DetailView):
  model = Item

class ItemDelete(DeleteView):
    model = Item
    success_message = 'Item deleted successfully!'
    success_url = reverse_lazy('items:item-list')

    def delete(self, request, *args, **kwargs):
      messages.success(self.request, self.success_message)
      return super(ItemDelete, self).delete(request, *args, **kwargs)