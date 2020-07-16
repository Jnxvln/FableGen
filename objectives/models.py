from django.db import models

# Create your models here.
class Objective(models.Model):
  name = models.CharField(max_length=200, blank=False, null=False, default='')
  quest = models.ForeignKey('quests.Quest', on_delete=models.SET_NULL, null=True, blank=True)
  completed = models.BooleanField(default=False)

  def print_quest(self):
    return type(self.quest)

  def __str__(self):
    return self.name

