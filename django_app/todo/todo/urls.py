from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from todo_list.views import NoteApiView
from todo_list import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('admin/', admin.site.urls),

    path('delete/<list_id>', views.delete, name="delete"), #delete with the item ID
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('edit/<list_id>', views.edit, name='edit'),

    path('api/', include('todo_list.urls')),
]


