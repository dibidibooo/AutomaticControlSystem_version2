from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import UpdateView

from tasks.forms import TaskUpdateForm
from ..models import Component, TaskAssign, Status


class TaskCreate:
    # 1|1
    def site1_task(self, form):
        oil_prod = Component.objects.get(title__contains='[1|1] Нефтепродукты')
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
        oil_prod = Component.objects.get(title__contains='[1|2] Нефтепродукты')
        ph = Component.objects.get(title__contains='[1|2] Значение рН')
        suspended_solids = Component.objects.get(title__contains='[1|2] Общие взвешенные твердые частицы')

        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(hours=oil_prod.period_in_hours)
            TaskAssign.objects.create(
                task=oil_prod.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=2,
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
                sampling_site_id=2,
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
                sampling_site_id=2,
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
                sampling_site_id=2,
                notification_id=1,
                plant_unit_id=1
            )

    # 1|3
    def site3_task(self, form):
        ph = Component.objects.get(title__contains='[1|3] Значение рН')
        suspended_subst = Component.objects.get(title__contains='[1|3] Взвешенные вещества')
        alkalinity = Component.objects.get(title__contains='[1|3] Щелочность общая')
        salt = Component.objects.get(title__contains='[1|3] Солесодержание')
        chlorides = Component.objects.get(title__contains='[1|3] Хлориды')
        sulfates = Component.objects.get(title__contains='[1|3] Сульфаты')

        if float(form.cleaned_data['suspended_subst']) > float(suspended_subst.limit_hi):
            comp_title = suspended_subst.title[6:]
            deadline = datetime.now() + timedelta(hours=suspended_subst.period_in_hours)
            TaskAssign.objects.create(
                task=suspended_subst.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=3,
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
                sampling_site_id=3,
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
                sampling_site_id=3,
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
                sampling_site_id=3,
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
                sampling_site_id=3,
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
                sampling_site_id=3,
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
                sampling_site_id=3,
                notification_id=1,
                plant_unit_id=1
            )

    # 2|1
    def site4_task(self, form):
        pass

    # 2|2
    def site5_task(self, form):
        hardness = Component.objects.get(title__contains='[2|2] Жесткость общая')
        hardness_calcium = Component.objects.get(title__contains='[2|2] Жесткость кальциеваяН')
        ph = Component.objects.get(title__contains='[2|2] Значение рН')
        salt = Component.objects.get(title__contains='[2|2] Солесодержание')
        chlorides = Component.objects.get(title__contains='[2|2] Хлориды')
        sulfates = Component.objects.get(title__contains='[2|2] Сульфаты')
        oil_prod = Component.objects.get(title__contains='[2|2] Нефтепродукты')
        suspended_subst = Component.objects.get(title__contains='[2|2] Взвешенные вещества')
        alkalinity = Component.objects.get(title__contains='[2|2] Щелочность общая')

        if float(form.cleaned_data['hardness']) > float(hardness.limit_hi):
            comp_title = hardness.title[6:]
            deadline = datetime.now() + timedelta(hours=hardness.period_in_hours)
            TaskAssign.objects.create(
                task=hardness.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['hardness_calcium']) > float(hardness_calcium.limit_hi):
            comp_title = hardness_calcium.title[6:]
            deadline = datetime.now() + timedelta(hours=hardness_calcium.period_in_hours)
            TaskAssign.objects.create(
                task=hardness_calcium.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=5,
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
                sampling_site_id=5,
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
                sampling_site_id=5,
                notification_id=2,
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
                sampling_site_id=5,
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
                sampling_site_id=5,
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
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(hours=oil_prod.period_in_hours)
            TaskAssign.objects.create(
                task=oil_prod.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['suspended_subst']) > float(suspended_subst.limit_hi):
            comp_title = suspended_subst.title[6:]
            deadline = datetime.now() + timedelta(hours=suspended_subst.period_in_hours)
            TaskAssign.objects.create(
                task=suspended_subst.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=5,
                notification_id=1,
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
                sampling_site_id=5,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['alkalinity']) < float(alkalinity.limit_lo):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(hours=alkalinity.period_in_hours)
            TaskAssign.objects.create(
                task=alkalinity.recommendation1,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=5,
                notification_id=2,
                plant_unit_id=1
            )

    # 3|1
    def site6_task(self, form):
        hardness = Component.objects.get(title__contains='[3|1] Жесткость общая')
        hardness_calcium = Component.objects.get(title__contains='[3|1] Жесткость кальциевая')
        ph = Component.objects.get(title__contains='[3|1] Значение рН')
        salt = Component.objects.get(title__contains='[3|1] Солесодержание')
        chlorides = Component.objects.get(title__contains='[3|1] Хлориды')
        sulfates = Component.objects.get(title__contains='[3|1] Сульфаты')
        oil_prod = Component.objects.get(title__contains='[3|1] Нефтепродукты')
        suspended_subst = Component.objects.get(title__contains='[3|1] Взвешенные вещества')
        alkalinity = Component.objects.get(title__contains='[3|1] Щелочность общая')

        if float(form.cleaned_data['hardness']) > float(hardness.limit_hi):
            comp_title = hardness.title[6:]
            deadline = datetime.now() + timedelta(hours=hardness.period_in_hours)
            TaskAssign.objects.create(
                task=hardness.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['hardness_calcium']) > float(hardness_calcium.limit_hi):
            comp_title = hardness_calcium.title[6:]
            deadline = datetime.now() + timedelta(hours=hardness_calcium.period_in_hours)
            TaskAssign.objects.create(
                task=hardness_calcium.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=6,
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
                sampling_site_id=6,
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
                sampling_site_id=6,
                notification_id=2,
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
                sampling_site_id=6,
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
                sampling_site_id=6,
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
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(hours=oil_prod.period_in_hours)
            TaskAssign.objects.create(
                task=oil_prod.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['suspended_subst']) > float(suspended_subst.limit_hi):
            comp_title = suspended_subst.title[6:]
            deadline = datetime.now() + timedelta(hours=suspended_subst.period_in_hours)
            TaskAssign.objects.create(
                task=suspended_subst.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=6,
                notification_id=1,
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
                sampling_site_id=6,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['alkalinity']) < float(alkalinity.limit_lo):
            comp_title = alkalinity.title[6:]
            deadline = datetime.now() + timedelta(hours=alkalinity.period_in_hours)
            TaskAssign.objects.create(
                task=alkalinity.recommendation1,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=6,
                notification_id=2,
                plant_unit_id=1
            )

    # 4|1
    def site7_task(self, form):
        pass

    # 4|2
    def site8_task(self, form):
        pass

    # 4|3
    def site9_task(self, form):
        suspended_solids = Component.objects.get(title__contains='[4|3] Общие взвешенные твердые частицы')
        chlorides = Component.objects.get(title__contains='[4|3] Хлориды')
        sulfates = Component.objects.get(title__contains='[4|3] Сульфаты')
        ph = Component.objects.get(title__contains='[4|3] Значение рН')
        phosphorus = Component.objects.get(title__contains='[4|3] Фосфор')
        alkalinity = Component.objects.get(title__contains='[4|3] Щелочность общая')
        salt = Component.objects.get(title__contains='[4|3] Солесодержание')

        if float(form.cleaned_data['suspended_solids']) > float(suspended_solids.limit_hi):
            comp_title = suspended_solids.title[6:]
            deadline = datetime.now() + timedelta(hours=suspended_solids.period_in_hours)
            TaskAssign.objects.create(
                task=suspended_solids.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=9,
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
                sampling_site_id=9,
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
                sampling_site_id=9,
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
                sampling_site_id=9,
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
                sampling_site_id=9,
                notification_id=2,
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
                sampling_site_id=9,
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
                sampling_site_id=9,
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
                sampling_site_id=9,
                notification_id=1,
                plant_unit_id=1
            )

    # 4|4
    def site10_task(self, form):
        chlorine = Component.objects.get(title__contains='[4|4] Остаточный хлор')
        oil_prod = Component.objects.get(title__contains='[4|4] Нефтепродукты')
        salt = Component.objects.get(title__contains='[4|4] Солесодержание')

        if float(form.cleaned_data['chlorine']) > float(chlorine.limit_hi):
            comp_title = chlorine.title[6:]
            deadline = datetime.now() + timedelta(hours=chlorine.period_in_hours)
            TaskAssign.objects.create(
                task=chlorine.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=10,
                notification_id=1,
                plant_unit_id=1
            )
        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(hours=oil_prod.period_in_hours)
            TaskAssign.objects.create(
                task=oil_prod.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=10,
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
                sampling_site_id=10,
                notification_id=1,
                plant_unit_id=1
            )

    # 4|5
    def site11_task(self, form):
        suspended_solids = Component.objects.get(title__contains='[4|5] Общие взвешенные твердые частицы')

        if float(form.cleaned_data['suspended_solids']) > float(suspended_solids.limit_hi):
            comp_title = suspended_solids.title[6:]
            deadline = datetime.now() + timedelta(hours=suspended_solids.period_in_hours)
            TaskAssign.objects.create(
                task=suspended_solids.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=11,
                notification_id=1,
                plant_unit_id=1
            )

    # 5|1
    def site12_task(self, form):
        oil_prod = Component.objects.get(title__contains='[5|1] Нефтепродукты')

        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(hours=oil_prod.period_in_hours)
            TaskAssign.objects.create(
                task=oil_prod.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=12,
                notification_id=1,
                plant_unit_id=1
            )

    # 6|1
    def site13_task(self, form):
        oil_prod = Component.objects.get(title__contains='[6|1] Нефтепродукты')
        ph = Component.objects.get(title__contains='[6|1] Значение рН')

        if float(form.cleaned_data['oil_prod']) > float(oil_prod.limit_hi):
            comp_title = oil_prod.title[6:]
            deadline = datetime.now() + timedelta(hours=oil_prod.period_in_hours)
            TaskAssign.objects.create(
                task=oil_prod.recommendation2,
                user_id=1,
                deadline=deadline,
                comp_title=comp_title,
                sampling_site_id=13,
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
                sampling_site_id=13,
                notification_id=1,
                plant_unit_id=1
            )

    # 5|2
    def site14_task(self, form):
        pass


class TaskUpdateView(UpdateView):
    model = TaskAssign
    template_name = 'tasks/task_update.html'
    context_object_name = 'task'
    form_class = TaskUpdateForm

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['users'] = User.objects.all()
        return context

    def get_success_url(self):
        return reverse('tasks-kanbanboard')