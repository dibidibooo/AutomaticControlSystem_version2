from datetime import datetime
from time import sleep

from django.http import JsonResponse, Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from allauth.account.views import PasswordSetView, PasswordChangeView
from django.urls import reverse_lazy

from tasks.models import Task, Comment, ChangesTracker
from projects.views.analysis import ResultsView


class DashboardView(PermissionRequiredMixin, View):
    permission_required = 'sites.view_site'

    def get(self, request):
        tasks = Task.objects.all()
        context = {}
        context['heading'] = "Страница CEO"
        context['pageview'] = "Главная"
        context['tasks'] = tasks
        context['overdue'] = self.get_overdue_tasks()
        context['on_time'] = self.get_on_time_tasks()
        context['escalated'] = self.get_escalated_tasks()

        context['log'] = GetUserInteractionsLog.get_log_info()  # Вывод данных с лог файла
        self.get_escalated_tasks()

        # Сравнение показателей с оборотной воды и с подпиточной воды на БОВ-2
        res = ResultsView()
        unit3_comparison = res.unit3_results_comparison()
        if unit3_comparison:
            context['unit_3_warning'] = unit3_comparison[0]
            context['dd'] = unit3_comparison[1]

        return render(request, 'dashboard/dashboard.html', context)

    def post(self, request):
        # Редактирование карточки задачи
        if 'edittask' in request.POST:
            id = request.POST['id']
            deadline = request.POST['deadline']
            status = request.POST['status']
            user = request.POST['user']
            task = Task.objects.get(id=id)
            task.deadline = deadline
            task.status_id = int(status)
            try:
                task.user_id = int(user)
            except ValueError:
                raise Http404('Пользователь не назначен!')

            if task.tracker.has_changed('status_id'):
                ChangesTracker.objects.create(
                    task_id=task.id,
                    text="изменил статус на",
                    who_changed=request.user,
                    changed_to=task.status
                )
            if task.tracker.has_changed('user_id'):
                ChangesTracker.objects.create(
                    task_id=task.id,
                    text="изменил исполнителя на",
                    who_changed=request.user,
                    changed_to=f"{task.user.profile.position}, {task.user.first_name} {task.user.last_name}"
                )
            if task.deadline:
                previous_date = task.tracker.previous('deadline').strftime('%Y-%m-%d %H:%M')
                current_date = " ".join(task.deadline.split("T"))
                if task.tracker.has_changed('deadline') and (previous_date != current_date):
                    ChangesTracker.objects.create(
                        task_id=task.id,
                        text="изменил срок исполнения на",
                        who_changed=request.user,
                        changed_to=datetime.strptime(task.deadline, '%Y-%m-%dT%H:%M').strftime('%Y-%m-%d %H:%M'),
                        failure_reason=request.POST['failure_reason']
                    )

            task.save()
            return redirect('dashboard')

        # Добавление комментариев
        elif 'add_comment_button' in request.POST:
            id = request.POST['id']
            task = Task.objects.get(id=id)
            comment = Comment.objects.create(
                text=request.POST.get('text'),
                task=task,
                author=self.request.user
            )
            return redirect('dashboard')
        else:
            # Изменение статуса при перетаскивании (drag and drop) карточки задачи
            status_id = int(request.POST.get('status'))
            task_id = int(request.POST.get('task_id'))
            task = get_object_or_404(Task, pk=task_id)
            task.status_id = status_id
            if task.status_id == 4:
                task.completion_date = datetime.now()
            task.save()
        return JsonResponse({"message": "success"})

    @staticmethod
    def get_overdue_tasks():
        overdue = 0
        for task in Task.objects.all():
            if datetime.now() > task.deadline:
                overdue += 1
        return overdue

    @staticmethod
    def get_on_time_tasks():
        on_time = 0
        for task in Task.objects.all():
            if task.completion_date and (task.completion_date <= task.deadline):
                on_time += 1
        return on_time

    @staticmethod
    def get_escalated_tasks():
        changes_history = ChangesTracker.objects.filter(changed_to__icontains='директор')
        changes_list = []
        for item in changes_history:
            changes_list.append(item.task_id)
        escalated = len(set(changes_list))
        return escalated


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard')


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('dashboard')


class GetUserInteractionsLog:
    @staticmethod
    def get_log_info():
        with open('users_interactions.log', encoding='utf-8') as f:
            log_items_list = [i.strip('\n') for i in f.readlines()]
            return log_items_list[::-1]
