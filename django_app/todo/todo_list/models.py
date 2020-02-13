#This is where the models for your app are located.

from django.db import models
from todo import settings


class List(models.Model):
    item = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
    # createdOn = models.DateTimeField(auto_now_add = True)

    # user_note = models.ForeignKey(
    #     # settings.AUTH_USER_MODEL,
    #     on_delete = models.CASCADE
    # )

    def __str__(self):
        return self.item + ' | ' + str(self.completed)


# # Create your models here.
# class NotesFeedItem(models.Model):


