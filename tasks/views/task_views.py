from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView

from projects.models import (
    Status,
    Component,
    ComponentsSite1,
    ComponentsSite2,
    ComponentsSite3,
    ComponentsSite4,
    ComponentsSite5,
    ComponentsSite6,
    ComponentsSite7,
    ComponentsSite8,
    ComponentsSite9,
    ComponentsSite10,
    ComponentsSite11,
    ComponentsSite12,
    ComponentsSite13,
    ComponentsSite14,
    ComponentsSite15,
    ComponentsSite16,
)
from tasks.forms import TaskForm
from tasks.models import Task, Comment, ChangesTracker


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/update.html'
    context_object_name = 'task'
    success_url = 'tasks-kanbanboard'
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['users'] = User.objects.all()
        context['changes'] = ChangesTracker.objects.filter(task_id=self.object.id)
        return context


class KanbanBoardView(PermissionRequiredMixin, View):
    permission_required = ('projects.view_task',)

    def get(self, request, *args, **kwargs):
        context = {
            'heading': "Kanban доска",
            'pageview': "Задачи",
            'tasks': Task.objects.all().order_by('start_date'),
            'statuses': Status.objects.all(),
            'users': User.objects.all(),
        }
        return render(request, 'tasks/kanbanboard.html', context)

    def post(self, request):
        if 'edittask' in request.POST:
            id = request.POST['id']
            deadline = request.POST.get('deadline')
            status = request.POST['status']
            user = request.POST['user']
            task = Task.objects.get(id=id)
            task.deadline = deadline
            task.status_id = int(status)
            task.user_id = int(user)

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
                    changed_to=f"{task.user}"
                )

            if task.deadline:
                previous_date = task.tracker.previous('deadline').strftime('%Y-%m-%d %H:%M')
                current_date = " ".join(task.deadline.split("T"))
                if task.tracker.has_changed('deadline') and (previous_date != current_date):
                    ChangesTracker.objects.create(
                        task_id=task.id,
                        text="изменил срок исполнения на",
                        who_changed=request.user,
                        changed_to=task.deadline,
                        failure_reason=request.POST['failure_reason']
                    )
            task.save()
            return redirect('tasks-kanbanboard')
        elif 'add_comment_button' in request.POST:
            id = request.POST['id']
            task = Task.objects.get(id=id)
            comment = Comment.objects.create(
                text=request.POST.get('text'),
                task=task,
                author=self.request.user
            )
            return redirect('tasks-kanbanboard')
        else:
            status_id = int(request.POST.get('status'))
            task_id = int(request.POST.get('task_id'))
            task = get_object_or_404(Task, pk=task_id)
            task.status_id = status_id

            if task.status_id == 4:
                task.completion_date = datetime.now()
            if task.tracker.has_changed('status_id'):
                ChangesTracker.objects.create(
                    task_id=task.id,
                    text="изменил статус на",
                    who_changed=request.user,
                    changed_to=task.status
                )
            task.save()
        return JsonResponse({"message": "success"})


class TaskCreate:
    # 1|1
    def site1_task(self, form, water_type):
        oil_prod = Component.objects.get(title__contains='[1|1] Нефтепродукт')
        ph = Component.objects.get(title__contains='[1|1] Значение рН')
        suspended_solids = Component.objects.get(title__contains='[1|1] Общие взвешенные твердые частицы')
        phosphorus = Component.objects.get(title__contains='[1|1] Фосфор')
        alkalinity = Component.objects.get(title__contains='[1|1] Щелочность общая')
        salt = Component.objects.get(title__contains='[1|1] Солесодержание')
        chlorides = Component.objects.get(title__contains='[1|1] Хлориды')
        sulfates = Component.objects.get(title__contains='[1|1] Сульфаты')

        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=oil_prod.recommendation2,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('oil_prod').latest('datetime')['oil_prod']),
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation2,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) < float(ph.limit_lo):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation1,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=1,
                notification_id=2,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['suspended_solids']) > float(suspended_solids.limit_hi):
            comp_title = suspended_solids.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=suspended_solids.recommendation2,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('suspended_solids').latest('datetime')['suspended_solids']),
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['phosphorus']) < float(phosphorus.limit_lo):
            comp_title = phosphorus.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=phosphorus.recommendation1,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('phosphorus').latest('datetime')['phosphorus']),
                sampling_site_id=1,
                notification_id=2,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['alkalinity']) > float(alkalinity.limit_hi):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=alkalinity.recommendation2,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('alkalinity').latest('datetime')['alkalinity']),
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['salt']) > float(salt.limit_hi):
            comp_title = salt.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=salt.recommendation2,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('salt').latest('datetime')['salt']),
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['chlorides']) > float(chlorides.limit_hi):
            comp_title = chlorides.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=chlorides.recommendation2,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('chlorides').latest('datetime')['chlorides']),
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['sulfates']) > float(sulfates.limit_hi):
            comp_title = sulfates.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=sulfates.recommendation2,
                responsible_id=3,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite1.objects.values('sulfates').latest('datetime')['sulfates']),
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )

    # 1|2
    def site2_task(self, form, water_type):
        oil_prod = Component.objects.get(title__contains='[1|2] Нефтепродукт')
        ph = Component.objects.get(title__contains='[1|2] Значение рН')
        suspended_solids = Component.objects.get(title__contains='[1|2] Общие взвешенные твердые частицы')

        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=oil_prod.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite2.objects.values('oil_prod').latest('datetime')['oil_prod']),
                sampling_site_id=2,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite2.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=2,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) < float(ph.limit_lo):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite2.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=2,
                notification_id=2,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['suspended_solids']) > float(suspended_solids.limit_hi):
            comp_title = suspended_solids.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=suspended_solids.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite2.objects.values('suspended_solids').latest('datetime')['suspended_solids']),
                sampling_site_id=2,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )

    # 1|3
    def site3_task(self, form, water_type):
        ph = Component.objects.get(title__contains='[1|3] Значение рН')
        suspended_subst = Component.objects.get(title__contains='[1|3] Взвешенные вещества')
        alkalinity = Component.objects.get(title__contains='[1|3] Щелочность общая')
        salt = Component.objects.get(title__contains='[1|3] Солесодержание')
        chlorides = Component.objects.get(title__contains='[1|3] Хлориды')
        sulfates = Component.objects.get(title__contains='[1|3] Сульфаты')

        if float(form.cleaned_data['suspended_subst']) > float(suspended_subst.limit_hi):
            comp_title = suspended_subst.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=suspended_subst.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite3.objects.values('suspended_subst').latest('datetime')['suspended_subst']),
                sampling_site_id=3,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite3.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=3,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) < float(ph.limit_lo):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite3.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=3,
                notification_id=2,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['alkalinity']) > float(alkalinity.limit_hi):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=alkalinity.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite3.objects.values('alkalinity').latest('datetime')['alkalinity']),
                sampling_site_id=3,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['salt']) > float(salt.limit_hi):
            comp_title = salt.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=salt.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite3.objects.values('salt').latest('datetime')['salt']),
                sampling_site_id=3,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['chlorides']) > float(chlorides.limit_hi):
            comp_title = chlorides.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=chlorides.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite3.objects.values('chlorides').latest('datetime')['chlorides']),
                sampling_site_id=3,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )
        if float(form.cleaned_data['sulfates']) > float(sulfates.limit_hi):
            comp_title = sulfates.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=sulfates.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite3.objects.values('sulfates').latest('datetime')['sulfates']),
                sampling_site_id=3,
                notification_id=1,
                plant_unit_id=1,
                water_type_id=water_type
            )

    # 2|1
    def site4_task(self, form, water_type):
        pass

    # 2|2
    def site5_task(self, form, water_type):
        hardness = Component.objects.get(title__contains='[2|2] Жесткость общая')
        hardness_calcium = Component.objects.get(title__contains='[2|2] Жесткость кальциевая')
        ph = Component.objects.get(title__contains='[2|2] Значение рН')
        salt = Component.objects.get(title__contains='[2|2] Солесодержание')
        chlorides = Component.objects.get(title__contains='[2|2] Хлориды')
        sulfates = Component.objects.get(title__contains='[2|2] Сульфаты')
        oil_prod = Component.objects.get(title__contains='[2|2] Нефтепродукт')
        suspended_subst = Component.objects.get(title__contains='[2|2] Взвешенные вещества')
        alkalinity = Component.objects.get(title__contains='[2|2] Щелочность общая')

        if float(form.cleaned_data['hardness']) > float(hardness.limit_hi):
            comp_title = hardness.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=hardness.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('hardness').latest('datetime')['hardness']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['hardness_calcium']) > float(hardness_calcium.limit_hi):
            comp_title = hardness_calcium.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=hardness_calcium.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('hardness_calcium').latest('datetime')['hardness_calcium']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) < float(ph.limit_lo):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=5,
                notification_id=2,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['salt']) > float(salt.limit_hi):
            comp_title = salt.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=salt.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('salt').latest('datetime')['salt']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['chlorides']) > float(chlorides.limit_hi):
            comp_title = chlorides.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=chlorides.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('chlorides').latest('datetime')['chlorides']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['sulfates']) > float(sulfates.limit_hi):
            comp_title = sulfates.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=sulfates.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('sulfates').latest('datetime')['sulfates']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=oil_prod.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('oil_prod').latest('datetime')['oil_prod']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['suspended_subst']) > float(suspended_subst.limit_hi):
            comp_title = suspended_subst.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=suspended_subst.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('suspended_subst').latest('datetime')['suspended_subst']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['alkalinity']) > float(alkalinity.limit_hi):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=alkalinity.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('alkalinity').latest('datetime')['alkalinity']),
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=2,
                water_type_id=water_type
            )
        if float(form.cleaned_data['alkalinity']) < float(alkalinity.limit_lo):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=alkalinity.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite5.objects.values('alkalinity').latest('datetime')['alkalinity']),
                sampling_site_id=5,
                notification_id=2,
                plant_unit_id=2,
                water_type_id=water_type
            )

    # 3|1
    def site6_task(self, form, water_type):
        hardness = Component.objects.get(title__contains='[3|1] Жесткость общая')
        hardness_calcium = Component.objects.get(title__contains='[3|1] Жесткость кальциевая')
        ph = Component.objects.get(title__contains='[3|1] Значение рН')
        salt = Component.objects.get(title__contains='[3|1] Солесодержание')
        chlorides = Component.objects.get(title__contains='[3|1] Хлориды')
        sulfates = Component.objects.get(title__contains='[3|1] Сульфаты')
        oil_prod = Component.objects.get(title__contains='[3|1] Нефтепродукт')
        suspended_subst = Component.objects.get(title__contains='[3|1] Взвешенные вещества')
        alkalinity = Component.objects.get(title__contains='[3|1] Щелочность общая')

        if float(form.cleaned_data['hardness']) > float(hardness.limit_hi):
            comp_title = hardness.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=hardness.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('hardness').latest('datetime')['hardness']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['hardness_calcium']) > float(hardness_calcium.limit_hi):
            comp_title = hardness_calcium.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=hardness_calcium.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('hardness_calcium').latest('datetime')['hardness_calcium']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) < float(ph.limit_lo):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=6,
                notification_id=2,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['salt']) > float(salt.limit_hi):
            comp_title = salt.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=salt.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('salt').latest('datetime')['salt']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['chlorides']) > float(chlorides.limit_hi):
            comp_title = chlorides.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=chlorides.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('chlorides').latest('datetime')['chlorides']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['sulfates']) > float(sulfates.limit_hi):
            comp_title = sulfates.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=sulfates.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('sulfates').latest('datetime')['sulfates']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=oil_prod.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('oil_prod').latest('datetime')['oil_prod']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['suspended_subst']) > float(suspended_subst.limit_hi):
            comp_title = suspended_subst.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=suspended_subst.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('suspended_subst').latest('datetime')['suspended_subst']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['alkalinity']) > float(alkalinity.limit_hi):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=alkalinity.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('alkalinity').latest('datetime')['alkalinity']),
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=3,
                water_type_id=water_type
            )
        if float(form.cleaned_data['alkalinity']) < float(alkalinity.limit_lo):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=alkalinity.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite6.objects.values('alkalinity').latest('datetime')['alkalinity']),
                sampling_site_id=6,
                notification_id=2,
                plant_unit_id=3,
                water_type_id=water_type
            )

    # 4|1
    def site7_task(self, form, water_type):
        pass

    # 4|2
    def site8_task(self, form, water_type):
        pass

    # 4|3
    def site9_task(self, form, water_type):
        suspended_solids = Component.objects.get(title__contains='[4|3] Общие взвешенные твердые частицы')
        chlorides = Component.objects.get(title__contains='[4|3] Хлориды')
        sulfates = Component.objects.get(title__contains='[4|3] Сульфаты')
        ph = Component.objects.get(title__contains='[4|3] Значение рН')
        phosphorus = Component.objects.get(title__contains='[4|3] Фосфор')
        alkalinity = Component.objects.get(title__contains='[4|3] Щелочность общая')
        salt = Component.objects.get(title__contains='[4|3] Солесодержание')

        if float(form.cleaned_data['suspended_solids']) > float(suspended_solids.limit_hi):
            comp_title = suspended_solids.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=suspended_solids.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('suspended_solids').latest('datetime')['suspended_solids']),
                sampling_site_id=9,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['chlorides']) > float(chlorides.limit_hi):
            comp_title = chlorides.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=chlorides.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('chlorides').latest('datetime')['chlorides']),
                sampling_site_id=9,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['sulfates']) > float(sulfates.limit_hi):
            comp_title = sulfates.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=sulfates.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('sulfates').latest('datetime')['sulfates']),
                sampling_site_id=9,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=9,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) < float(ph.limit_lo):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=9,
                notification_id=2,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['phosphorus']) < float(phosphorus.limit_lo):
            comp_title = phosphorus.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=phosphorus.recommendation1,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('phosphorus').latest('datetime')['phosphorus']),
                sampling_site_id=9,
                notification_id=2,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['alkalinity']) > float(alkalinity.limit_hi):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=alkalinity.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('alkalinity').latest('datetime')['alkalinity']),
                sampling_site_id=9,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['salt']) > float(salt.limit_hi):
            comp_title = salt.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=salt.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite9.objects.values('salt').latest('datetime')['salt']),
                sampling_site_id=9,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )

    # 4|4
    def site10_task(self, form, water_type):
        chlorine = Component.objects.get(title__contains='[4|4] Остаточный хлор')
        oil_prod = Component.objects.get(title__contains='[4|4] Нефтепродукт')
        salt = Component.objects.get(title__contains='[4|4] Солесодержание')

        if float(form.cleaned_data['chlorine']) > float(chlorine.limit_hi):
            comp_title = chlorine.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=chlorine.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite10.objects.values('chlorine').latest('datetime')['chlorine']),
                sampling_site_id=10,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=oil_prod.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite10.objects.values('oil_prod').latest('datetime')['oil_prod']),
                sampling_site_id=10,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )
        if float(form.cleaned_data['salt']) > float(salt.limit_hi):
            comp_title = salt.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=salt.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite10.objects.values('salt').latest('datetime')['salt']),
                sampling_site_id=10,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )

    # 4|5
    def site11_task(self, form, water_type):
        suspended_solids = Component.objects.get(title__contains='[4|5] Общие взвешенные твердые частицы')

        if float(form.cleaned_data['suspended_solids']) > float(suspended_solids.limit_hi):
            comp_title = suspended_solids.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=suspended_solids.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite11.objects.values('suspended_solids').latest('datetime')['suspended_solids']),
                sampling_site_id=11,
                notification_id=1,
                plant_unit_id=4,
                water_type_id=water_type
            )

    # 5|1
    def site12_task(self, form, water_type):
        oil_prod = Component.objects.get(title__contains='[5|1] Нефтепродукт')

        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=oil_prod.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite12.objects.values('oil_prod').latest('datetime')['oil_prod']),
                sampling_site_id=12,
                notification_id=1,
                plant_unit_id=5,
                water_type_id=water_type
            )

    # 6|1
    def site13_task(self, form, water_type):
        oil_prod = Component.objects.get(title__contains='[6|1] Нефтепродукт')
        ph = Component.objects.get(title__contains='[6|1] Значение рН')

        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=oil_prod.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite13.objects.values('oil_prod').latest('datetime')['oil_prod']),
                sampling_site_id=13,
                notification_id=1,
                plant_unit_id=6,
                water_type_id=water_type
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(days=3)
            Task.objects.create(
                title=ph.recommendation2,
                responsible_id=1,
                deadline=deadline,
                comp_title=comp_title,
                comp_value=int(ComponentsSite13.objects.values('ph').latest('datetime')['ph']),
                sampling_site_id=13,
                notification_id=1,
                plant_unit_id=6,
                water_type_id=water_type
            )

    # 6|2
    def site14_task(self, form, water_type):
        pass


    # 6|2
    def site15_task(self, form, water_type):
        pass


    # 6|2
    def site16_task(self, form, water_type):
        pass


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