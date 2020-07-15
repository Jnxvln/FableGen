from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Location

# Create your views here.
class LocationList(ListView):
  model = Location
  context_object_name = 'locations'

class LocationCreate(CreateView):
  model = Location
  fields = '__all__'

class LocationDetail(DetailView):
  model = Location

class LocationDelete(DeleteView):
    model = Location
    success_message = 'Location deleted successfully!'
    success_url = reverse_lazy('locations:location-list')

    def delete(self, request, *args, **kwargs):
      messages.success(self.request, self.success_message)
      return super(LocationDelete, self).delete(request, *args, **kwargs)