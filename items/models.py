from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default='')

  def get_absolute_url(self):
    return reverse('items:item-detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.name

