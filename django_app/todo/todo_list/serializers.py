from rest_framework import serializers
from todo_list.models import List


class NoteSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    class Meta:
        model = List
        fields = ('id', 'todo_text', 'done')


class NoteApiSerializer(serializers.ModelSerializer):
   class Meta:
       model = List
       fields = '__all__'



