#This is where the models for your app are located.

from django.db import models
from todo import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


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




class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    # user = models.ForeignKey(AbstractBaseUser, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text


class List(models.Model):
    item = models.CharField(max_length = 200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)



