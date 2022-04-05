from django.urls import path

from projects.views.tasks import TaskUpdateView
from tasks import views

urlpatterns = [
    path('tasklist', views.TaskListView.as_view(), name='tasks-tasklist'),
    path('kanbanboard', views.KanbanBoardView.as_view(), name='tasks-kanbanboard'),
    path('createtask', views.CreateTaskView.as_view(), name='tasks-createtask'),
    path('kanbanboard/<int:pk>', TaskUpdateView.as_view(), name='tasks-updatetask'),
]