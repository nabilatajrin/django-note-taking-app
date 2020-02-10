# This deals with how you want to view your models in the django admin. admin.py is where you register your app’s models
# with the Django admin application. admin.py − This file helps you make the app modifiable in the admin interface.

from django.contrib import admin
from . models import List

# Register your models here.
admin.site.register(List)
