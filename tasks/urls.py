from django.urls import path

from tasks.views.comment_views import CommentCreateView
from tasks.views.task_views import TaskListView, KanbanBoardView, CreateTaskView, TaskDetailView

urlpatterns = [
    path('tasklist', TaskListView.as_view(), name='tasks-tasklist'),
    path('kanbanboard', KanbanBoardView.as_view(), name='tasks-kanbanboard'),
    path('createtask', CreateTaskView.as_view(), name='tasks-createtask'),
    path('<int:pk>', TaskDetailView.as_view(), name='tasks-detail'),
    path('<int:pk>/comment/add', CommentCreateView.as_view(), name='comments-add'),
]