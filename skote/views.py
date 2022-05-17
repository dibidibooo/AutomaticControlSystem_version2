from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordSetView, PasswordChangeView
from django.urls import reverse_lazy

from tasks.models import Task, Comment, ChangesTracker


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {}
        context['heading'] = "Страница CEO"
        context['pageview'] = "Главная"
        context['tasks'] = tasks
        context['overdue'] = self.get_overdue_tasks()
        context['on_time'] = self.get_on_time_tasks()
        context['escalated'] = self.get_escalated_tasks()
        self.get_escalated_tasks()
        return render(request, 'dashboard/dashboard.html', context)

    def post(self, request):
        if 'edittask' in request.POST:
            id = request.POST['id']
            deadline = request.POST['deadline']
            status = request.POST['status']
            user = request.POST['user']
            task = Task.objects.filter(id=id)
            task.update(deadline=deadline, status=status, user_id=int(user))
            return redirect('dashboard')
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
            if task.completion_date and (task.completion_date > task.deadline):
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
        changes_history = ChangesTracker.objects.filter(text__contains='изменил исполнителя на director')
        changes_list = []
        for item in changes_history:
            changes_list.append(item.task_id)
        escalated = len(set(changes_list))
        return escalated


# Authentication
# class PagesLoginView(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-login.html')
#
#
# class PagesRegisterView(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-register.html')
#
#
# class PagesRecoverpwView(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-recoverpw.html')
#
#
# class PagesLockscreenView(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-lockscreen.html')
#
#
# class PagesConfirmmailView(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-confirmmail.html')
#
#
# class PagesEmailVerificationView(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-emailverificationmail.html')
#
#
# class PagesTwoStepVerificationView(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-twostepverificationmail.html')
#
#
# class PagesLogin2View(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-login-2.html')
#
#
# class PagesRegister2View(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-register-2.html')
#
#
# class PagesRecoverpw2View(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-recoverpw2.html')
#
#
# class PagesLockscreen2View(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-lockscreen2.html')
#
#
# class PagesConfirmmail2View(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-confirmmail-2.html')
#
#
# class PagesEmailVerification2View(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-emailverificationmail-2.html')
#
#
# class PagesTwoStepVerification2View(View):
#     def get(self, request):
#         return render(request, 'authentication/pages-twostepverificationmail-2.html')


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard')


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('dashboard')
