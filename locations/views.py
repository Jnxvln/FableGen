from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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

