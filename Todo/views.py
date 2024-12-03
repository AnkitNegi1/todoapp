from django.shortcuts import render
from Todo.models import TodoData
from rest_framework import generics
from Todo.serializers import TodoSerializer


# Create your views here.

class ListTodo(generics.ListAPIView):
    queryset = TodoData.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = TodoData.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = TodoData.objects.all()
    serializer_class = TodoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = TodoData.objects.all()
    serializer_class = TodoSerializer

