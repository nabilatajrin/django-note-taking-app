#This is where the models for your app are located.

from django.db import models
from todo import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class List(models.Model):
    item = models.CharField(max_length = 200)
    completed = models.BooleanField(default=False)
    # createdOn = models.DateTimeField(auto_now_add = True)

    # user_note = models.ForeignKey(
    #     # settings.AUTH_USER_MODEL,
    #     on_delete = models.CASCADE
    # )

    def __str__(self):
        return self.item + ' | ' + str(self.completed)


# # Create your models here.
# class NotesFeedItem(models.Model):


class AddNote(models.Model):
    note = models.CharField(max_length=255)
    # completed = models.BooleanField(default=False)
    # created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return str(self.note)


class TestNote(models.Model):
    title = models.CharField(max_length=100)


class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    # author = models.ForeignKey('Author', related_name='articles')

    def __str__(self):
        return self.title




