from rest_framework import serializers, viewsets

from todo_list import models
from todo_list.models import List

class NoteSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    class Meta:
        model = List
        fields = ('id', 'todo_text', 'done')

class ContactSerializer(serializers.ModelSerializer):
   class Meta:
       model = List
       fields = '__all__'



