from rest_framework import serializers
from Todo.models import TodoData

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoData
        fields = '__all__'
        read_only_fields = ['todotimestamp']
