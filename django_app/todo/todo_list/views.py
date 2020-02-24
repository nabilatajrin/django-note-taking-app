# views.py is where the views for your app are located.

# A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response.
# This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image,
# etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.

from django.shortcuts import render, redirect
from rest_framework.settings import api_settings
from .forms import NoteForm
from django.contrib import messages
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets
from .models import List
from .serializers import ContactSerializer


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = NoteForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added to list!'))
            return redirect('home')
    else:
        all_items = List.objects.all
        return render(request, "home.html", {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = NoteForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            #all_items = Note.objects.all
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


#-------------------------------API--------------------------------------
class ContactViewSet(viewsets.ModelViewSet):
   serializer_class = ContactSerializer
   queryset = List.objects.all()

   # def delete(self, request, *args, **kwargs):
   #     return self.destroy(request, *args, **kwargs)


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES