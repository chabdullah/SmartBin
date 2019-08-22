from django.db import models

# Create your models here.

import datetime
from django.utils import timezone

class Materials(models.Model):
    material = models.CharField(max_length=20)
    def __str__(self):
        return self.material
    
class ThrownTrash(models.Model):
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    thrown_date = models.DateTimeField('when it was thrown')
    
    def was_thrown_within_the_last_day(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.thrown_date <= timezone.now()