from django.db import models
from items.models import Item

class Reward(models.Model):
  entity = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, blank=True)
  quantity = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)
  quest = models.ForeignKey('quests.Quest', on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    label = '{}x{}'.format(self.quantity, self.entity.name)
    return label

