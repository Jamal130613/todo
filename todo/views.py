from django.shortcuts import render
from rest_framework.generics import *
from todo.models import Task
from todo.serializers import TaskSerializer


# class TaskListView(ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskCreateView(CreateAPIView):
#     serializer_class = TaskSerializer
#
#
# class TaskDetailView(RetrieveAPIView):
#     lookup_field = 'id'
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskUpdateView(UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskDeleteView(DestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
