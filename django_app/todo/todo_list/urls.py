# It helps to connect the view to a url. We want to access that view via a URL. Django has his own way for URL mapping
# and it's done by editing your project url.py file.

# urls.py contains project-level URL configurations. By default, this contains a single URL pattern for the admin.
from django.db import router
from django.urls import path, include
from django.contrib import admin
from todo_list import views
# from . import views

urlpatterns = [
    path('hello-view/', views.NoteApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),

]
