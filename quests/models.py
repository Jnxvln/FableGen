from django.db import models
from objectives.models import Objective
from rewards.models import Reward
from django.urls import reverse


class Quest(models.Model):
  name = models.CharField(max_length=150, blank=False, null=False, default='')
  story = models.TextField(blank=False, null=False, default='')

  @property
  def objectives(self):
    queryset = Objective.objects.filter(quest__name=self.name)
    objs = list(queryset)
    return objs

  @property
  def rewards(self):
    queryset = Reward.objects.filter(quest__name=self.name)
    rewards = list(queryset)
    return rewards

  def get_absolute_url(self):
    return reverse('quests:quest-detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.name
  
