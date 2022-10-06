from ctypes.wintypes import MAX_PATH
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Pepper(models.Model):
    common_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=150)
    scoville = models.IntegerField()
    img = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['scoville']
