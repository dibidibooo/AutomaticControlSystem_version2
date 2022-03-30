from datetime import datetime, timedelta

from ..models import Component, TaskAssign


class TaskCreate:
    # 1|1
    def site1_task(self, form):
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
            deadline = datetime.now() + timedelta(hours=oil_prod.period_in_hours)
            TaskAssign.objects.create(
                task=oil_prod.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['ph']) > float(ph.limit_hi):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(hours=ph.period_in_hours)
            TaskAssign.objects.create(
                task=ph.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['ph']) < float(ph.limit_lo):
            comp_title = ph.title[6:]
            deadline = datetime.now() + timedelta(hours=ph.period_in_hours)
            TaskAssign.objects.create(
                task=ph.recommendation1,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=2,
                plant_unit_id=1
            )
        if float(form.cleaned_data['suspended_solids']) > float(suspended_solids.limit_hi):
            comp_title = suspended_solids.title[6:]
            deadline = datetime.now() + timedelta(hours=suspended_solids.period_in_hours)
            TaskAssign.objects.create(
                task=suspended_solids.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['phosphorus']) < float(phosphorus.limit_lo):
            comp_title = phosphorus.title[6:]
            deadline = datetime.now() + timedelta(hours=phosphorus.period_in_hours)
            TaskAssign.objects.create(
                task=phosphorus.recommendation1,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=2,
                plant_unit_id=1
            )
        if float(form.cleaned_data['alkalinity']) > float(alkalinity.limit_hi):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(hours=alkalinity.period_in_hours)
            TaskAssign.objects.create(
                task=alkalinity.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['salt']) > float(salt.limit_hi):
            comp_title = salt.title[6:]
            deadline = datetime.now() + timedelta(hours=salt.period_in_hours)
            TaskAssign.objects.create(
                task=salt.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['chlorides']) > float(chlorides.limit_hi):
            comp_title = chlorides.title[6:]
            deadline = datetime.now() + timedelta(hours=chlorides.period_in_hours)
            TaskAssign.objects.create(
                task=chlorides.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['sulfates']) > float(sulfates.limit_hi):
            comp_title = sulfates.title[6:]
            deadline = datetime.now() + timedelta(hours=sulfates.period_in_hours)
            TaskAssign.objects.create(
                task=sulfates.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1,
                notification_id=1,
                plant_unit_id=1
            )

    # 1|2
    def site2_task(self, form):
        if float(form.cleaned_data['oil_prod']) > float(Component.objects.get(title__contains='[1|2] Нефтепродукт').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|2] Нефтепродукт').title[6:]
            task = Task.objects.get(pk=3)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=2
            )
        if float(form.cleaned_data['ph']) > float(Component.objects.get(title__contains='[1|2] Значение рН').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|2] Значение рН').title[6:]
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=2
            )
        if float(form.cleaned_data['ph']) < float(Component.objects.get(title__contains='[1|2] Значение рН').limit_lo):
            comp_title = Component.objects.get(title__contains='[1|2] Значение рН').title[6:]
            task = Task.objects.get(pk=15)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=2
            )
        if float(form.cleaned_data['suspended_solids']) > float(Component.objects.get(title__contains='[1|2] Общие взвешенные твердые частицы').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|2] Общие взвешенные твердые частицы').title[6:]
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=2
            )

    # 1|3
    def site3_task(self, form):
        if float(form.cleaned_data['suspended_subst']) > float(Component.objects.get(title__contains='[1|3] Взвешенные вещества').limit_hi):
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline
            )
        if float(form.cleaned_data['ph']) > float(Component.objects.get(title__contains='[1|3] Значение рН').limit_hi):
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline
            )
        if float(form.cleaned_data['ph']) < float(Component.objects.get(title__contains='[1|3] Значение рН').limit_lo):
            task = Task.objects.get(pk=15)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline
            )
        if float(form.cleaned_data['alkalinity']) > float(Component.objects.get(title__contains='[1|3] Щелочность общая').limit_hi):
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline
            )
        if float(form.cleaned_data['salt']) > float(Component.objects.get(title__contains='[1|3] Солесодержание').limit_hi):
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline
            )
        if float(form.cleaned_data['chlorides']) > float(Component.objects.get(title__contains='[1|3] Хлориды').limit_hi):
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline
            )
        if float(form.cleaned_data['sulfates']) > float(Component.objects.get(title__contains='[1|3] Сульфаты').limit_hi):
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline
            )