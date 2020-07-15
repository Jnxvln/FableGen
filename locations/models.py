from django.db import models
from django.urls import reverse

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default='')
  backstory = models.TextField(blank=True, null=True, default='')

  def get_absolute_url(self):
    return reverse('locations:location-detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.name

