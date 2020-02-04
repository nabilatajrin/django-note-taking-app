# This deals with how you want to view your models in the django admin. admin.py is where you register your app’s models
# with the Django admin application.

# This file helps you make the app modifiable in the admin interface.

from django import forms
from .models import List

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]







