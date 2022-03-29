from datetime import datetime, timedelta

from ..models import Component, Task, TaskAssign


class TaskCreate:
    # 1|1
    def site1_task(self, form):
        if float(form.cleaned_data['oil_prod']) > float(Component.objects.get(title__contains='[1|1] Нефтепродукт').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|1] Нефтепродукт').title[6:]
            task = Task.objects.get(pk=3)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        if float(form.cleaned_data['ph']) > float(Component.objects.get(title__contains='[1|1] Значение рН').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|1] Значение рН').title[6:]
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        if float(form.cleaned_data['ph']) < float(Component.objects.get(title__contains='[1|1] Значение рН').limit_lo):
            comp_title = Component.objects.get(title__contains='[1|1] Значение рН').title[6:]
            task = Task.objects.get(pk=15)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        if float(form.cleaned_data['suspended_solids']) > float(Component.objects.get(title__contains='[1|1] Общие взвешенные твердые частицы').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|1] Общие взвешенные твердые частицы').title[6:]
            task = Task.objects.get(pk=6)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        if float(form.cleaned_data['phosphorus']) < float(Component.objects.get(title__contains='[1|1] Фосфор').limit_lo):
            comp_title = Component.objects.get(title__contains='[1|1] Фосфор').title[6:]
            task = Task.objects.get(pk=4)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        if float(form.cleaned_data['alkalinity']) > float(Component.objects.get(title__contains='[1|1] Щелочность общая').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|1] Щелочность общая').title[6:]
            task = Task.objects.get(pk=3)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        # if float(form.cleaned_data['hardness']) < float(Component.objects.get(title__contains='[1|1] Жесткость общая').limit_lo):
        #     task = Task.objects.get(pk=3)
        #     deadline = datetime.now() + timedelta(hours=task.execution_period)
        #     TaskAssign.objects.create(
        #         task_id=task.id,
        #         user_id=1,
        #         deadline=deadline
        #     )
        if float(form.cleaned_data['salt']) > float(Component.objects.get(title__contains='[1|1] Солесодержание').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|1] Солесодержание').title[6:]
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        if float(form.cleaned_data['chlorides']) > float(Component.objects.get(title__contains='[1|1] Хлориды').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|1] Хлориды').title[6:]
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
            )
        if float(form.cleaned_data['sulfates']) > float(Component.objects.get(title__contains='[1|1] Сульфаты').limit_hi):
            comp_title = Component.objects.get(title__contains='[1|1] Сульфаты').title[6:]
            task = Task.objects.get(pk=13)
            deadline = datetime.now() + timedelta(hours=task.execution_period)
            TaskAssign.objects.create(
                task_id=task.id,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=1
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
