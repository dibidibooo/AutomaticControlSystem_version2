from django.urls import path

from tasks.views.comment_views import CommentCreateView
from tasks.views.task_views import (
    ArchiveTaskListView,
    KanbanBoardView,
    TaskUpdateView,
    TaskDetailView
)

urlpatterns = [
    path('tasklist', ArchiveTaskListView.as_view(), name='tasks-tasklist'),
    path('kanbanboard', KanbanBoardView.as_view(), name='tasks-kanbanboard'),
    path('<int:pk>', TaskUpdateView.as_view(), name='tasks-update'),
    path('detail/<int:pk>', TaskDetailView.as_view(), name='tasks-detail'),
    path('kanbanboard/<int:pk>', CommentCreateView.as_view(), name='comments-add'),
]
