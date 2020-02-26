#This is where the models for your app are located.

from django.db import models


# Create your models here.
class List(models.Model):
    item = models.CharField(max_length = 200)
    completed = models.BooleanField(default=False)

    # Pythonic way to convert Python objects into strings by using __str__.
    def __str__(self):
        return self.item + ' | ' + str(self.completed)



