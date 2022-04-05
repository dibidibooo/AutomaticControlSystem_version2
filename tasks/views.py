from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.
from projects.models import TaskAssign


class KanbanBoardView(PermissionRequiredMixin, View):
    permission_required = ('projects.view_taskassign',)

    def get(self, request):
        context = {
            'heading': "Kanban Board",
            'pageview': "Tasks",
            'tasks': TaskAssign.objects.all()
        }
        return render(request, 'tasks/kanbanboard.html', context)

    def post(self, request):
        status_id = int(request.POST.get('status'))
        task_id = int(request.POST.get('task_id'))
        task = get_object_or_404(TaskAssign, pk=task_id)
        task.status_id = status_id
        task.save()
        return JsonResponse({"message": "success"})


class TaskListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'heading': "Task List",
            'pageview': "Tasks"
        }
        return render(request, 'tasks/tasklist.html', context)


class CreateTaskView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'heading': "Create Task",
            'pageview': "Tasks"
        }
        return render(request, 'tasks/createtask.html', context)