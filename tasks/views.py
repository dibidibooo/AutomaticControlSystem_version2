from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from projects.models import TaskAssign, Status


class KanbanBoardView(PermissionRequiredMixin, View):
    permission_required = ('projects.view_taskassign',)
    context = {}

    # def dispatch(self, request, *args, **kwargs):
    #     if 'taskid' in request.GET:
    #         self.context['task'] = TaskAssign.objects.get(id=request.GET.get('taskid'))
    #         print(self.context)
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        self.context = {
            'heading': "Kanban доска",
            'pageview': "Задачи",
            'tasks': TaskAssign.objects.all(),
            'statuses': Status.objects.all(),
            'users': User.objects.all(),
        }
        if 'taskid' in request.GET:
            self.context['task'] = TaskAssign.objects.get(id=request.GET.get('taskid'))
            print(self.context)
        return render(request, 'tasks/kanbanboard.html', self.context)

    def post(self, request):
        if 'edittask' in request.POST:
            id = request.POST['id']
            deadline = request.POST['deadline']
            status = request.POST['status']
            user = request.POST['user']

            task = TaskAssign.objects.filter(id=id)
            task.update(deadline=deadline, status=status, user_id=int(user))
            return redirect('tasks-kanbanboard')
        else:
            status_id = int(request.POST.get('status'))
            task_id = int(request.POST.get('task_id'))
            task = get_object_or_404(TaskAssign, pk=task_id)
            task.status_id = status_id
            task.save()
            return JsonResponse({"message": "success"})

    def get_update_modal(self, request):
        if request.GET.get('taskid'):
            task_id = request.GET.get('taskid')
            print(task_id)
            context = {
                'heading': "Kanban доска",
                'pageview': "Задачи",
                'tasks': TaskAssign.objects.all(),
                'statuses': Status.objects.all(),
                'users': User.objects.all(),
                'task': TaskAssign.objects.get(id=int(task_id)),
            }
            print(context)
            return render(request, 'tasks/kanbanboard.html', context)


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
