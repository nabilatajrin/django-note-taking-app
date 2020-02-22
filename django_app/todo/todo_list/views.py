# views.py is where the views for your app are located.

# A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response.
# This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image,
# etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.settings import api_settings

from .models import List, TestNote, Article
from .forms import NoteForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets

from todo_list.serializers import NoteSerializer
from todo_list import models, serializers
from .serializers import ArticleSerializer
from todo_list import permissions


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


# class NoteApiView(APIView):
#     def get(self, request):
#         serializer = List()
#
#         # return Response(serializer.data)
#         return Response({'test': 'It worked!'})


"""API"""

class Get_collection(APIView): #err
    def get(self, request):
        if request.method == 'GET':
            posts = List.objects.all()
            serializer = NoteSerializer(posts, many=True)
            return Response(serializer.data)



class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class AddNoteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AddNoteApiSerializer
    queryset = models.List.objects.all()

    # """Handles creating, reading and updating profile feed items"""
    # authentication_classes = (TokenAuthentication,)
    # serializer_class = serializers.NoteSerializer
    # queryset = models.AddNote.objects.all()
    #
    # def perform_create(self, serializer):
    #     """Sets the user profile to the logged in user"""
    #     serializer.save(user_profile=self.request.user)


class TestNoteViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = serializers.List

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(title=self.request.user)


# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         return Response({"articles": articles})


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)