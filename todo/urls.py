from django.urls import path
from todo.views import *

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view()),
#     path('', TaskListView.as_view()),
#     path('create/', TaskCreateView.as_view()),
#     path('detail/<int:id>/', TaskDetailView.as_view()),
#     path('update/<int:pk>/', TaskUpdateView.as_view()),
#     path('delete/<int:pk>/', TaskDeleteView.as_view())
]
