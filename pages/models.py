from django.db import models
from datetime import datetime
# Create your models here.

class Msglist(models.Model):
    name = models.CharField(max_length=200)
    list_date= models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    