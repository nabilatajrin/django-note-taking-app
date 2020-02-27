# It helps to connect the view to a url. We want to access that view via a URL. Django has his own way for URL mapping
# and it's done by editing your project url.py file.

# urls.py contains project-level URL configurations. By default, this contains a single URL pattern for the admin.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo_list import views
from todo_list.views import NoteViewSet


router = DefaultRouter() #create viewsets in views
router.register('notes', NoteViewSet)


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    # path('someurl', views.ProfileList.as_view()),
    path('', include(router.urls))

]
