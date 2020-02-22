# It helps to connect the view to a url. We want to access that view via a URL. Django has his own way for URL mapping
# and it's done by editing your project url.py file.

# urls.py contains project-level URL configurations. By default, this contains a single URL pattern for the admin.
from django.db import router
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from todo_list import views
# from . import views
from todo_list.views import ArticleView

router = DefaultRouter() #create viewsets in views
router.register('add-note', views.AddNoteViewSet, basename='add-note')
router.register('test-note', views.TestNoteViewSet, basename='test-note')

# router.register('list', views.AddNoteViewSet, basename='list')
# router.register('edit', views.AddNoteViewSet, basename='edit')
# router.register('delete', views.AddNoteViewSet, basename='delete')

urlpatterns = [
    # path('hello-view/', views.NoteApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('add-note/', views.Get_collection.as_view()),
    path('test-note/', views.Get_collection.as_view()),
    # path('list/', views.Get_collection.as_view()),
    # path('edit/', views.Get_collection.as_view()),
    # path('delete/', views.Get_collection.as_view()),
    path('articles/', ArticleView.as_view()),

    path('', include(router.urls))
]
