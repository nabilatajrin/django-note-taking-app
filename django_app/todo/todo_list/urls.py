# It helps to connect the view to a url. We want to access that view via a URL. Django has his own way for URL mapping
# and it's done by editing your project url.py file.

# urls.py contains project-level URL configurations. By default, this contains a single URL pattern for the admin.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('delete/<list_id>', views.delete, name="delete"), #delete with the item ID
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('edit/<list_id>', views.edit, name='edit'),
]
