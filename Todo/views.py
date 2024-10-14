from django.shortcuts import render
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework import viewsets
# Create your views here.
class TodoItemViewSet(viewsets.ModelViewSet):
    
    queryset=TodoItem.objects.all()
    serializer_class=TodoItemSerializer