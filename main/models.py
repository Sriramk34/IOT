from pydoc import describe
from django.db import models

class devices(models.Model):
    name = models.CharField(max_length=25)
    status = models.BooleanField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"Name:{self.name}   Description:{self.description}"