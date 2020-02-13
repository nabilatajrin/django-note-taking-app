from rest_framework import serializers
from todo_list.models import List

class NoteSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

    class Meta:
        model = List
        fields = 'id', 'todo_text', 'done'
