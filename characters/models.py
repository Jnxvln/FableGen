from django.db import models
from django.urls import reverse

GENDER = [
  (None, 'Choose'),
  ('male', 'Male'),
  ('female', 'Female'),
  ('notspecified', 'Not Specified')
]

# Create your models here.
class Character(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, default='')
  gender = models.CharField(max_length=50, choices=GENDER, blank=False, null=False, default=None)

  def get_absolute_url(self):
    return reverse('characters:character-detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.name

