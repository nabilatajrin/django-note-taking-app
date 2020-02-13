# views.py is where the views for your app are located.

# A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response.
# This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image,
# etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.

from django.shortcuts import render, redirect
from rest_framework.settings import api_settings

from .models import List
from .forms import ListForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets

from todo_list.serializers import NoteSerializer
from todo_list import models
# from todo_list import permissions


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

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

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            #all_items = List.objects.all
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


class NoteApiView(APIView):
    def get(self, request):
        serializer = List()

        return Response(serializer.data)
        # return Response({'test': 'It worked!'})



    """test APIView"""
    # serializers_class = serializers.HelloSerializer
    #
    # def get(self, request, format=None):
    #     """returns a list of APIView features"""
    #     an_apiview = [
    #         'Uses HTTP methods as function(get, post, patch, put, delete)',
    #     ]
    #     return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    #
    # def post(self, request):
    #     """create a hello message with our name"""
    #     serializer = self.serializers_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         name = serializer.validated_data.get('name')
    #         message = f'Hello{name}'
    #         return Response({'message': message})
    #     else:
    #         return Response(
    #             serializer.errors,
    #             status = status.HTTP_400_BAD_REQUEST
    #         )
    #
    # def delete(selfself, request, pk):
    #     """Delete an object"""
    #     item = List.objects.get(pk=pk)
    #     item.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #     # return Response({'method': 'DELETE'})


class UserLoginApiView(ObtainAuthToken):
    """handle user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



