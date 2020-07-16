from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Place

# Create your views here.
class PlaceList(ListView):
  model = Place
  context_object_name = 'places'

class PlaceCreate(CreateView):
  model = Place
  fields = '__all__'

class PlaceDetail(DetailView):
  model = Place

class PlaceUpdate(SuccessMessageMixin, UpdateView):
  model = Place
  fields = '__all__'
  success_message = '%(name)s updated successfully!'

class PlaceDelete(DeleteView):
  model = Place
  success_message = '{place} deleted successfully!'
  success_url = reverse_lazy('places:place-list')

  def delete(self, request, *args, **kwargs):
    place = Place.objects.get(pk=kwargs.get('pk'))
    self.success_message = f'{place} deleted successfully!'
    messages.success(self.request, self.success_message)
    return super(PlaceDelete, self).delete(request, *args, **kwargs)