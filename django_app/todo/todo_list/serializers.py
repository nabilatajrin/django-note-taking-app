from rest_framework import serializers, viewsets

from todo_list import models
from todo_list.models import List, TestNote


class NoteSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    # name = serializers.CharField(max_length=10)

    class Meta:
        model = List
        fields = ('id', 'todo_text', 'done')



class AddNoteApiSerializer(serializers.Serializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.TestNote
        fields = ('id', 'note')
        # extra_kwargs = {
        #     'password': {
        #         'write_only': True,
        #         'style': {'input_type': 'password'}
        #     }
        # }

    # def create(self, validated_data):
    #     """Create and return a new post"""
    #     user = models.AddNote.objects.create_user(
    #         note = validated_data['note']
    #     )
    #
    #     return user

    #AddNote in model

class TestNoteSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestNote
        fields = ('id', 'title')


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()


