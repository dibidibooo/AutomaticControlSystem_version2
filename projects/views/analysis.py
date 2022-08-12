from datetime import datetime
import logging
from collections import defaultdict

from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView

from tasks.models import Task, Comment, ChangesTracker
from tasks.views.task_views import TaskCreate

from projects.forms import (
    Site1Form,
    Site2Form,
    Site3Form,
    Site4Form,
    Site5Form,
    Site6Form,
    Site7Form,
    Site8Form,
    Site9Form,
    Site10Form,
    Site11Form,
    Site12Form,
    Site13Form,
    Site14Form,
    Site15Form,
    Site16Form,
    AdditionalAnalysisForm,
)
from projects.models import (
    ComponentsSite,
    Component,
    AdditionalComponents,
    PlantUnit,
    AdditionalCalculations, ComponentFormula
)
from projects.multiforms import MultiFormsView


user_logger = logging.getLogger('users_interactions')


class AnalysisCreateView(PermissionRequiredMixin, MultiFormsView):
    permission_required = ('projects.add_componentssite',)
    template_name = "projects/analyses_create.html"
    form_classes = {
        'site1': Site1Form,
        'site2': Site2Form,
        'site3': Site3Form,
        'site4': Site4Form,
        'site5': Site5Form,
        'site6': Site6Form,
        'site7': Site7Form,
        'site8': Site8Form,
        'site9': Site9Form,
        'site10': Site10Form,
        'site11': Site11Form,
        'site12': Site12Form,
        'site13': Site13Form,
        'site14': Site14Form,
        'site15': Site15Form,
        'site16': Site16Form,
    }

    success_url = reverse_lazy('analyzes_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Загрузка анализов'
        context['pageview'] = 'Анализы'
        context['components'] = Component.objects.all()
        context['tasks'] = Task.objects.all()
        if self.request.user.username != 'admin':
            user_logger.info(f'Пользователь {self.request.user.first_name} {self.request.user.last_name} '
                             f'(@{self.request.user}) был на странице загрузки анализов.')
        return context

    # Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
    def site1_form_valid(self, form):
        oil_prod = form.cleaned_data.get('oil_prod')
        suspended_solids = form.cleaned_data.get('suspended_solids')
        ph = form.cleaned_data.get('ph')
        phosphorus = form.cleaned_data.get('phosphorus')
        alkalinity = form.cleaned_data.get('alkalinity')
        hardness = form.cleaned_data.get('hardness')
        salt = form.cleaned_data.get('salt')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        iron = form.cleaned_data.get('iron')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        hardness_magnesium = form.cleaned_data.get('hardness_magnesium')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 1

        ComponentsSite.objects.create(
            oil_prod=oil_prod,
            suspended_solids=suspended_solids,
            ph=ph,
            phosphorus=phosphorus,
            alkalinity=alkalinity,
            hardness=hardness,
            salt=salt,
            chlorides=chlorides,
            sulfates=sulfates,
            iron=iron,
            hardness_calcium=hardness_calcium,
            hardness_magnesium=hardness_magnesium,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site1_task(form, water_type, responsible_id=3)
        return HttpResponseRedirect(self.success_url)

    # Водоблок - 2 | Установка АВТ напротив погружного холодильника №42
    def site2_form_valid(self, form):
        oil_prod = form.cleaned_data.get('oil_prod')
        ph = form.cleaned_data.get('ph')
        suspended_solids = form.cleaned_data.get('suspended_solids')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 1

        ComponentsSite.objects.create(
            oil_prod=oil_prod,
            ph=ph,
            suspended_solids=suspended_solids,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site2_task(form, water_type, responsible_id=3)
        return HttpResponseRedirect(self.success_url)

    # Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-5,11.12
    def site3_form_valid(self, form):
        suspended_subst = form.cleaned_data.get('suspended_subst')
        hardness = form.cleaned_data.get('hardness')
        iron = form.cleaned_data.get('iron')
        dry_residue = form.cleaned_data.get('dry_residue')
        alkalinity = form.cleaned_data.get('alkalinity')
        salt = form.cleaned_data.get('salt')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        hardness_magnesium = form.cleaned_data.get('hardness_magnesium')
        ph = form.cleaned_data.get('ph')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 2

        ComponentsSite.objects.create(
            suspended_subst=suspended_subst,
            hardness=hardness,
            iron=iron,
            dry_residue=dry_residue,
            alkalinity=alkalinity,
            salt=salt,
            chlorides=chlorides,
            sulfates=sulfates,
            hardness_calcium=hardness_calcium,
            hardness_magnesium=hardness_magnesium,
            ph=ph,
            plant_unit_id=self.request.POST.get('plant_unit'),
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site3_task(form, water_type, responsible_id=3)
        return HttpResponseRedirect(self.success_url)

    # БОВ-1 | Аналитическая точка насосов Р-02А/В/С
    def site4_form_valid(self, form):
        hardness = form.cleaned_data.get('hardness')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        ph = form.cleaned_data.get('ph')
        salt = form.cleaned_data.get('salt')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        oil_prod = form.cleaned_data.get('oil_prod')
        suspended_subst = form.cleaned_data.get('suspended_subst')
        alkalinity = form.cleaned_data.get('alkalinity')
        iron = form.cleaned_data.get('iron')
        phosphorus = form.cleaned_data.get('phosphorus')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 2

        ComponentsSite.objects.create(
            hardness=hardness,
            hardness_calcium=hardness_calcium,
            ph=ph,
            salt=salt,
            chlorides=chlorides,
            sulfates=sulfates,
            oil_prod=oil_prod,
            suspended_subst=suspended_subst,
            alkalinity=alkalinity,
            iron=iron,
            phosphorus=phosphorus,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site4_task(form, water_type, responsible_id=3)
        return HttpResponseRedirect(self.success_url)

    # БОВ-1 | Аналитическая точка выкид насосов Р-01А/В/С/Д
    def site5_form_valid(self, form):
        hardness = form.cleaned_data.get('hardness')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        ph = form.cleaned_data.get('ph')
        salt = form.cleaned_data.get('salt')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        oil_prod = form.cleaned_data.get('oil_prod')
        suspended_subst = form.cleaned_data.get('suspended_subst')
        alkalinity = form.cleaned_data.get('alkalinity')
        iron = form.cleaned_data.get('iron')
        phosphorus = form.cleaned_data.get('phosphorus')
        halogen = form.cleaned_data.get('halogen')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 1

        ComponentsSite.objects.create(
            hardness=hardness,
            hardness_calcium=hardness_calcium,
            ph=ph,
            salt=salt,
            chlorides=chlorides,
            sulfates=sulfates,
            oil_prod=oil_prod,
            suspended_subst=suspended_subst,
            alkalinity=alkalinity,
            iron=iron,
            phosphorus=phosphorus,
            halogen=halogen,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site5_task(form, water_type, responsible_id=3)
        return HttpResponseRedirect(self.success_url)

    # БОВ-2 | Аналитическая точка насосов Р-01А/В/С/Д
    def site6_form_valid(self, form):
        hardness = form.cleaned_data.get('hardness')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        ph = form.cleaned_data.get('ph')
        salt = form.cleaned_data.get('salt')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        oil_prod = form.cleaned_data.get('oil_prod')
        suspended_subst = form.cleaned_data.get('suspended_subst')
        alkalinity_phenols = form.cleaned_data.get('alkalinity_phenols')
        alkalinity = form.cleaned_data.get('alkalinity')
        iron = form.cleaned_data.get('iron')
        phosphorus = form.cleaned_data.get('phosphorus')
        halogen = form.cleaned_data.get('halogen')
        form_name = form.cleaned_data.get('action')
        water_type = 1
        smpl_site = form.cleaned_data.get('smpl_site')

        ComponentsSite.objects.create(
            hardness=hardness,
            hardness_calcium=hardness_calcium,
            ph=ph,
            salt=salt,
            chlorides=chlorides,
            sulfates=sulfates,
            oil_prod=oil_prod,
            suspended_subst=suspended_subst,
            alkalinity_phenols=alkalinity_phenols,
            alkalinity=alkalinity,
            iron=iron,
            phosphorus=phosphorus,
            halogen=halogen,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site6_task(form, water_type, responsible_id=3)
        return HttpResponseRedirect(self.success_url)

    # УГОВ | Аналитическая точка насосов Р-01А/В/С/Д
    def site7_form_valid(self, form):
        suspended_solids = form.cleaned_data.get('suspended_solids')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        ph = form.cleaned_data.get('ph')
        alkalinity = form.cleaned_data.get('alkalinity')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        hardness = form.cleaned_data.get('hardness')
        iron = form.cleaned_data.get('iron')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 1

        ComponentsSite.objects.create(
            suspended_solids=suspended_solids,
            chlorides=chlorides,
            sulfates=sulfates,
            ph=ph,
            alkalinity=alkalinity,
            hardness_calcium=hardness_calcium,
            hardness=hardness,
            iron=iron,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site7_task(form, water_type, responsible_id=5)
        return HttpResponseRedirect(self.success_url)

    # УГОВ | Выход из ёмкости 77-ТК-103 77-SN-004
    def site8_form_valid(self, form):
        suspended_solids = form.cleaned_data.get('suspended_solids')
        ph = form.cleaned_data.get('ph')
        chlorides = form.cleaned_data.get('chlorides')
        phosphorus = form.cleaned_data.get('phosphorus')
        oil_prod = form.cleaned_data.get('oil_prod')
        alkalinity = form.cleaned_data.get('alkalinity')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        hardness = form.cleaned_data.get('hardness')
        iron = form.cleaned_data.get('iron')
        salt = form.cleaned_data.get('salt')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 2

        ComponentsSite.objects.create(
            suspended_solids=suspended_solids,
            ph=ph,
            chlorides=chlorides,
            phosphorus=phosphorus,
            oil_prod=oil_prod,
            alkalinity=alkalinity,
            hardness_calcium=hardness_calcium,
            hardness=hardness,
            iron=iron,
            salt=salt,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site8_task(form, water_type, responsible_id=5)
        return HttpResponseRedirect(self.success_url)

    # УГОВ | На входе в боковой фильтр позиции 77-Z-003 77-SN-006
    def site9_form_valid(self, form):
        suspended_solids = form.cleaned_data.get('suspended_solids')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        ph = form.cleaned_data.get('ph')
        phosphorus = form.cleaned_data.get('phosphorus')
        alkalinity = form.cleaned_data.get('alkalinity')
        hardness_calcium = form.cleaned_data.get('hardness_calcium')
        hardness = form.cleaned_data.get('hardness')
        iron = form.cleaned_data.get('iron')
        salt = form.cleaned_data.get('salt')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 1

        ComponentsSite.objects.create(
            suspended_solids=suspended_solids,
            chlorides=chlorides,
            sulfates=sulfates,
            ph=ph,
            phosphorus=phosphorus,
            alkalinity=alkalinity,
            hardness_calcium=hardness_calcium,
            hardness=hardness,
            iron=iron,
            salt=salt,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site9_task(form, water_type, responsible_id=5)
        return HttpResponseRedirect(self.success_url)

    # УГОВ | Подача на градирню в районе 77-ТI-205 77-SN-007
    def site10_form_valid(self, form):
        chlorine = form.cleaned_data.get('chlorine')
        oil_prod = form.cleaned_data.get('oil_prod')
        salt = form.cleaned_data.get('salt')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 1

        ComponentsSite.objects.create(
            chlorine=chlorine,
            oil_prod=oil_prod,
            salt=salt,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site10_task(form, water_type, responsible_id=5)
        return HttpResponseRedirect(self.success_url)

    # УГОВ | На выходе с бокового фильтра 77-Z-003, 77-SN-008
    def site11_form_valid(self, form):
        suspended_solids = form.cleaned_data.get('suspended_solids')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 1

        ComponentsSite.objects.create(
            suspended_solids=suspended_solids,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site11_task(form, water_type, responsible_id=5)
        return HttpResponseRedirect(self.success_url)

    # МОС -> Очистные сооружения поз.119. С колодца промстоков №1 (точка №4 вход)
    def site12_form_valid(self, form):
        oil_prod = form.cleaned_data.get('oil_prod')
        suspended_subst = form.cleaned_data.get('suspended_subst')
        ph = form.cleaned_data.get('ph')
        oxygen_chem = form.cleaned_data.get('oxygen_chem')
        active_subst = form.cleaned_data.get('active_subst')
        ammonium = form.cleaned_data.get('ammonium')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 3

        ComponentsSite.objects.create(
            oil_prod=oil_prod,
            suspended_subst=suspended_subst,
            ph=ph,
            oxygen_chem=oxygen_chem,
            active_subst=active_subst,
            ammonium=ammonium,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site12_task(form, water_type, responsible_id=6)
        return HttpResponseRedirect(self.success_url)

    # БОС -> Пробоотборник 001 перед БОС / А1–SN-001
    def site13_form_valid(self, form):
        oil_prod = form.cleaned_data.get('oil_prod')
        suspended_subst = form.cleaned_data.get('suspended_subst')
        ph = form.cleaned_data.get('ph')
        oxygen_chem = form.cleaned_data.get('oxygen_chem')
        active_subst = form.cleaned_data.get('active_subst')
        ammonium = form.cleaned_data.get('ammonium')
        oxygen_bio = form.cleaned_data.get('oxygen_bio')
        phenols = form.cleaned_data.get('phenols')
        chlorides = form.cleaned_data.get('chlorides')
        sulfates = form.cleaned_data.get('sulfates')
        iron = form.cleaned_data.get('iron')
        nitrate = form.cleaned_data.get('nitrate')
        nitrite = form.cleaned_data.get('nitrite')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 3

        ComponentsSite.objects.create(
            oil_prod=oil_prod,
            suspended_subst=suspended_subst,
            ph=ph,
            oxygen_chem=oxygen_chem,
            active_subst=active_subst,
            ammonium=ammonium,
            oxygen_bio=oxygen_bio,
            phenols=phenols,
            chlorides=chlorides,
            sulfates=sulfates,
            iron=iron,
            nitrate=nitrate,
            nitrite=nitrite,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site13_task(form, water_type, responsible_id=7)
        return HttpResponseRedirect(self.success_url)

    # БОС -> Сточная вода после биологических очистных сооружений А1–SN-009
    def site14_form_valid(self, form):
        alkalinity = form.cleaned_data.get('alkalinity')
        hardness = form.cleaned_data.get('hardness')
        oxidability = form.cleaned_data.get('oxidability')
        salt = form.cleaned_data.get('salt')
        chlorine = form.cleaned_data.get('chlorine')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 3

        ComponentsSite.objects.create(
            alkalinity=alkalinity,
            hardness=hardness,
            oxidability=oxidability,
            salt=salt,
            chlorine=chlorine,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site14_task(form, water_type, responsible_id=7)
        return HttpResponseRedirect(self.success_url)

    # БОС -> Выход с аппарата напорной флотации в ТК -008А/ А1–SN-004А
    def site15_form_valid(self, form):
        suspended_subst = form.cleaned_data.get('suspended_subst')
        oil_prod = form.cleaned_data.get('oil_prod')
        oxygen_chem = form.cleaned_data.get('oxygen_chem')
        ammonium = form.cleaned_data.get('ammonium')
        phosphorus = form.cleaned_data.get('phosphorus')
        oxygen_bio = form.cleaned_data.get('oxygen_bio')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 3

        ComponentsSite.objects.create(
            suspended_subst=suspended_subst,
            oil_prod=oil_prod,
            oxygen_chem=oxygen_chem,
            ammonium=ammonium,
            phosphorus=phosphorus,
            oxygen_bio=oxygen_bio,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site15_task(form, water_type, responsible_id=7)
        return HttpResponseRedirect(self.success_url)

    # БОС -> Выход с аппарата напорной флотации в ТК-008В/ А1 –SN -004В
    def site16_form_valid(self, form):
        suspended_subst = form.cleaned_data.get('suspended_subst')
        oil_prod = form.cleaned_data.get('oil_prod')
        oxygen_chem = form.cleaned_data.get('oxygen_chem')
        ammonium = form.cleaned_data.get('ammonium')
        phosphorus = form.cleaned_data.get('phosphorus')
        oxygen_bio = form.cleaned_data.get('oxygen_bio')
        form_name = form.cleaned_data.get('action')
        smpl_site = form.cleaned_data.get('smpl_site')
        water_type = 3

        ComponentsSite.objects.create(
            suspended_subst=suspended_subst,
            oil_prod=oil_prod,
            oxygen_chem=oxygen_chem,
            ammonium=ammonium,
            phosphorus=phosphorus,
            oxygen_bio=oxygen_bio,
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type,
            user=self.request.user
        )
        task_create = TaskCreate()
        task_create.site16_task(form, water_type, responsible_id=7)
        return HttpResponseRedirect(self.success_url)


class AdditionalAnalysisCreateView(PermissionRequiredMixin, CreateView):
    """Загрузка ежедневных параметров"""

    model = AdditionalComponents
    form_class = AdditionalAnalysisForm
    template_name = 'projects/additional_analyses_create.html'
    success_url = reverse_lazy('analyzes_results')
    permission_required = ('projects.add_additionalcomponents', )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Загрузка ежедневных параметров"
        context['pageview'] = "Анализы"
        context['plant_units'] = PlantUnit.objects.all()
        if self.request.user.username != 'admin':
            user_logger.info(f'Пользователь {self.request.user.first_name} {self.request.user.last_name} '
                             f'(@{self.request.user}) был на странице загрузки ежедневных параметров.')
        return context

    def form_valid(self, form):
        unit_id = self.request.POST.get('uid')
        unit = get_object_or_404(PlantUnit, pk=unit_id)
        form.instance.plant_unit = unit
        form.save()
        if int(unit_id) in range(1, 5):
            formula = AdditionalCalc()
            formula.calculations(unit=int(unit_id))
        return super().form_valid(form)


class AdditionalCalc:
    """Дополнительные расчеты по формулам"""

    def calculations(self, unit: int) -> None:
        smpl_site_recycled = self.sampling_site_recycled_water(unit)
        smpl_site_running = self.sampling_site_running_water(unit)

        running_water_consumption = AdditionalComponents.objects.all().last().running_water_consumption
        recycled_water_consumption = AdditionalComponents.objects.all().last().recycled_water_consumption

        # Коэффициент упаривания
        evaporation_ratio = self.evaporation_ratio(unit, smpl_site_recycled, smpl_site_running)

        # Транспорт кальциевой жесткости
        tr_ca = self.transport_ca(unit, smpl_site_recycled, smpl_site_running, evaporation_ratio)

        # Объем продувки фактический
        p3 = running_water_consumption / evaporation_ratio
        p3 = round(p3, 1)

        # Потери с испарением
        p1 = self.evaporation_loss(recycled_water_consumption)

        # Капельный унос
        p2 = recycled_water_consumption * 0.002
        p2 = round(p2, 1)

        # Объем продувки расчетный (теоретический)
        if unit == 4:
            salt_running_water = ComponentsSite.objects.filter(sampling_site_id=8).last().salt
        else:
            salt_running_water = ComponentsSite.objects.filter(sampling_site_id=smpl_site_running).last().salt
        x = (2000 / salt_running_water) - 1
        p3_calculated = (p1 / x) - p2
        p3_calculated = round(p3_calculated, 1)

        # Несанкционированные потери
        purge_flow = AdditionalComponents.objects.all().last().purge_flow
        unauthorized_loss = running_water_consumption - p1 - p2 - purge_flow
        unauthorized_loss = round(unauthorized_loss, 1)

        AdditionalCalculations.objects.create(
            evaporation_ratio=evaporation_ratio,
            calcium_hardness_transport=tr_ca,
            purge_volume=p3,
            evaporative_loss=p1,
            drip_loss=p2,
            unauthorized_loss=unauthorized_loss,
            plant_unit_id=unit
        )

    @staticmethod
    def evaporation_ratio(unit, smpl_site_recycled, smpl_site_running):
        # chlorides_recycled_water = ComponentsSite.objects.filter(
        #     sampling_site_id=smpl_site_recycled, plant_unit_id=unit
        # ).last().chlorides
        # if smpl_site_recycled == 6 and smpl_site_running == 4:
        #     chlorides_running_water = ComponentsSite.objects.filter(
        #         sampling_site_id=smpl_site_running, plant_unit_id=2
        #     ).last().chlorides
        # else:
        #     chlorides_running_water = ComponentsSite.objects.filter(
        #         sampling_site_id=smpl_site_running, plant_unit_id=unit
        #     ).last().chlorides
        # evaporation_ratio = chlorides_recycled_water / chlorides_running_water

        if unit == 1:
            hardness_magnesium_recycled_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_recycled, plant_unit_id=unit
            ).last().hardness_magnesium
            hardness_magnesium_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running, plant_unit_id=unit
            ).last().hardness_magnesium
        else:
            # Расчет Магниевой жесткости
            hardness_recycled_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_recycled, plant_unit_id=unit
            ).last().hardness
            hardness_calcium_recycled_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_recycled, plant_unit_id=unit
            ).last().hardness_calcium
            hardness_magnesium_recycled_water = hardness_recycled_water - hardness_calcium_recycled_water

            hardness_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running
            ).last().hardness
            hardness_calcium_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running
            ).last().hardness_calcium
            hardness_magnesium_running_water = hardness_running_water - hardness_calcium_running_water

        evaporation_ratio = hardness_magnesium_recycled_water / hardness_magnesium_running_water

        evaporation_ratio = round(evaporation_ratio, 1)
        return evaporation_ratio

    @staticmethod
    def transport_ca(unit, smpl_site_recycled, smpl_site_running, evaporation_ratio):
        calcium_recycled_water = ComponentsSite.objects.filter(
            sampling_site_id=smpl_site_recycled, plant_unit_id=unit).last().hardness_calcium
        if smpl_site_recycled == 6 and smpl_site_running == 4:
            calcium_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running, plant_unit_id=2).last().hardness_calcium
        else:
            calcium_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running, plant_unit_id=unit).last().hardness_calcium
        tr_ca = (calcium_recycled_water * 100) / (calcium_running_water * evaporation_ratio)
        tr_ca = round(tr_ca, 1)
        return tr_ca

    @staticmethod
    def evaporation_loss(recycled_water_consumption):
        hot_water_temp = AdditionalComponents.objects.all().last().hot_water_temp
        cold_water_temp = AdditionalComponents.objects.all().last().cold_water_temp
        delta_temp = hot_water_temp - cold_water_temp

        k = 0
        today = datetime.today()
        if today.month in range(6, 9):
            k = 0.15
        elif today.month in range(1, 3) or today.month == 12:
            k = 0.07
        elif today.month in range(3, 6) or today.month in range(9, 12):
            k = 0.1

        x = (delta_temp * k) / 100
        p1 = x * recycled_water_consumption
        p1 = round(p1, 1)
        return p1

    @staticmethod
    def sampling_site_recycled_water(unit: int) -> int:
        # Получение ID МОП, если тип воды - оборотная
        smpl_site = 0
        if unit == 1:
            smpl_site = 1
        elif unit == 2:
            smpl_site = 5
        elif unit == 3:
            smpl_site = 6
        elif unit == 4:
            smpl_site = 9
        return smpl_site

    @staticmethod
    def sampling_site_running_water(unit: int) -> int:
        # Получение ID МОП, если тип воды - подпиточная
        smpl_site = 0
        if unit == 1:
            smpl_site = 3
        elif unit == 2:
            smpl_site = 4
        elif unit == 3:
            smpl_site = 4
        elif unit == 4:
            smpl_site = 7
        return smpl_site


class ExcelTableView(PermissionRequiredMixin, View):
    permission_required = ['tasks.view_task']

    def get(self, request):
        context = {
            'heading': "Отчеты",
            'pageview': "Результаты",
            'tasks': Task.objects.order_by('start_date'),
            'results': ComponentsSite.objects.order_by('datetime'),
        }
        if self.request.user.username != 'admin':
            user_logger.info(f'Пользователь {self.request.user.first_name} {self.request.user.last_name} '
                             f'(@{self.request.user}) был на странице отчетов.')
        return render(request, 'projects/excel_table.html', context)


class ResultsView(PermissionRequiredMixin, View):
    permission_required = 'projects.view_componentssite'

    def get(self, request):
        tasks = Task.objects.order_by('start_date')
        notifications = Task.objects.order_by('-start_date')[:10]
        components = Component.objects.all()

        context = {
            'heading': "Результаты",
            'pageview': "Анализы",
            'components': components,
            'tasks': tasks,
            'notifications': notifications,
            'results1': self.get_results(1),
            'results2': self.get_results(2),
            'results3': self.get_results(3),
            'results4': self.get_results(4),
            'results5': self.get_results(5),
            'results6': self.get_results(6),
            'results7': self.get_results(7),
            'results8': self.get_results(8),
            'results9': self.get_results(9),
            'results10': self.get_results(10),
            'results11': self.get_results(11),
            'results12': self.get_results(12),
            'results13': self.get_results(13),
            'results14': self.get_results(14),
            'results15': self.get_results(15),
            'results16': self.get_results(16),
            'res_additional_1': self.get_add_results(1),
            'res_additional_2': self.get_add_results(2),
            'res_additional_3': self.get_add_results(3),
            'res_additional_4': self.get_add_results(4),
            'res_additional_5': self.get_add_results(5),
            'res_additional_6': self.get_add_results(6),
            'calculated_params1': AdditionalCalculations.objects.filter(plant_unit_id=1).last(),
            'calculated_params2': AdditionalCalculations.objects.filter(plant_unit_id=2).last(),
            'calculated_params3': AdditionalCalculations.objects.filter(plant_unit_id=3).last(),
            'calculated_params4': AdditionalCalculations.objects.filter(plant_unit_id=4).last(),
            'calc_params_recom1': self.get_calculated_params_recom(1),
            'calc_params_recom2': self.get_calculated_params_recom(2),
            'calc_params_recom3': self.get_calculated_params_recom(3),
            'calc_params_recom4': self.get_calculated_params_recom(4),
        }

        unit3_comparison = self.unit3_results_comparison()
        if unit3_comparison:
            context['unit_3_warning'] = unit3_comparison[0]
            context['dd'] = unit3_comparison[1]

        if self.request.user.username != 'admin':
            user_logger.info(f'Пользователь {self.request.user.first_name} {self.request.user.last_name} '
                             f'(@{self.request.user}) был на странице результатов.')
        return render(request, 'projects/analyses_results.html', context)

    def post(self, request):
        # Редактирование карточки задачи
        if 'edittask' in request.POST:
            task_id = request.POST['id']
            deadline = request.POST.get('deadline')
            status = request.POST['status']
            user = request.POST['user']
            task = Task.objects.get(id=task_id)
            task.deadline = deadline
            task.status_id = int(status)
            try:
                task.user_id = int(user)
            except ValueError:
                raise Http404('Пользователь не назначен!')
            if task.status_id == 4:
                task.completion_date = datetime.now()

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
            return redirect('analyzes_results')

        # Добавление комментариев
        elif 'add_comment_button' in request.POST:
            task_id = request.POST['id']
            task = Task.objects.get(id=task_id)
            comment = Comment.objects.create(
                text=request.POST.get('text'),
                task=task,
                author=self.request.user
            )
            return redirect('analyzes_results')
        return JsonResponse({"message": "success"})

    # Сравнение показателей с оборотной воды на БОВ-2 и с подпиточной воды на БОВ-1
    def unit3_results_comparison(self):
        dict1 = {}
        dict2 = {}
        if ComponentsSite.objects.filter(sampling_site_id=6) and \
                ComponentsSite.objects.filter(sampling_site_id=4):

            a = ComponentsSite.objects.filter(sampling_site_id=4).values().latest('datetime')
            b = ComponentsSite.objects.filter(sampling_site_id=6).values().latest('datetime')
            for key, value in a.items():
                if value and key and key != 'id' and key != 'datetime' and key != 'sampling_site_id' and \
                        key != 'water_type_id' and key != 'plant_unit' and key != 'halogen':
                    dict1[key] = value
            for key, value in b.items():
                if value and key and key != 'id' and key != 'datetime' and key != 'sampling_site_id' and \
                        key != 'water_type_id' and key != 'plant_unit' and key != 'alkalinity_phenols' and key != 'halogen':
                    dict2[key] = value

        diffkeys = [key for key in dict1 if dict1.get(key) == dict2.get(key) and dict1[key] > dict2[key]]
        bov1_dict = {}
        bov2_dict = {}

        for key in diffkeys:
            bov1_dict[key] = dict1[key]
            bov2_dict[key] = dict2[key]

        dd = defaultdict(list)
        for d in (bov1_dict, bov2_dict):
            for key, value in d.items():
                dd[key].append(value)

        compared_results = self.translate_comp_titles(dict(dd))

        if diffkeys:
            warning_text = """
            Показатели компонентов БОВ-2 с оборотной воды ниже показателей компонентов БОВ-1 с подпиточной воды.
            Пожалуйста, обратите внимание!
            """
            return warning_text, compared_results
        else:
            return None

    # Перевод названия компонентов на русский (т.к. названия берутся из названия столбцов в таблице)
    @staticmethod
    def translate_comp_titles(compared_dict):
        if 'phosphorus' in compared_dict:
            compared_dict['Фосфор'] = compared_dict.pop('phosphorus')
        if 'chlorides' in compared_dict:
            compared_dict['Хлориды'] = compared_dict.pop('chlorides')
        if 'iron' in compared_dict:
            compared_dict['Железо'] = compared_dict.pop('iron')
        if 'hardness_calcium' in compared_dict:
            compared_dict['Жёсткость кальциевая'] = compared_dict.pop('hardness_calcium')
        if 'hardness' in compared_dict:
            compared_dict['Жёсткость общая'] = compared_dict.pop('hardness')
        if 'alkalinity' in compared_dict:
            compared_dict['Щёлочность общая'] = compared_dict.pop('alkalinity')
        if 'ph' in compared_dict:
            compared_dict['Значение pH'] = compared_dict.pop('ph')
        if 'salt' in compared_dict:
            compared_dict['Солесодержание'] = compared_dict.pop('salt')
        if 'sulfates' in compared_dict:
            compared_dict['Сульфаты'] = compared_dict.pop('sulfates')
        if 'oil_prod' in compared_dict:
            compared_dict['Нефтепродукт'] = compared_dict.pop('oil_prod')
        if 'suspended_subst' in compared_dict:
            compared_dict['Общие взвешенные вещества'] = compared_dict.pop('suspended_subst')
        return compared_dict

    # Отображение результатов анализов доп. компонентов
    @staticmethod
    def get_add_results(unit_id):
        results = AdditionalComponents.objects.filter(plant_unit_id=unit_id)
        if results:
            return results.latest('datetime')

    # Отображение результатов основных анализов
    @staticmethod
    def get_results(site_id: int) -> dict:
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite.objects.filter(
                sampling_site_id=site_id).latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == site_id and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite.objects.filter(
                    sampling_site_id=site_id).values().latest('datetime').items():
                if key != 'id' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    # Вывод рекомендаций для рассчитываемых параметров
    @staticmethod
    def get_calculated_params_recom(unit_id):
        recommendations = {}
        calculated_params = AdditionalCalculations.objects.filter(plant_unit_id=unit_id).last()
        additional_comp_data = ComponentFormula.objects.all()
        for i in additional_comp_data:
            if unit_id in [2, 3] and 'Коэффициент упаривания БОВ-1/2' in i.title:
                if not calculated_params:
                    recommendations['no_data'] = 'Нет данных'
                if calculated_params and calculated_params.evaporation_ratio > float(i.limit_hi):
                    recommendations['Коэффициент упаривания БОВ-1/2'] = i.recommendation2
                elif calculated_params and calculated_params.evaporation_ratio < float(i.limit_lo):
                    recommendations['Коэффициент упаривания БОВ-1/2'] = i.recommendation1
                else:
                    recommendations['no_recom'] = 'В пределах нормы'
            if unit_id in [1, 4] and 'Коэффициент упаривания Водоблок/УГОВ' in i.title:
                if not calculated_params:
                    recommendations['no_data'] = 'Нет данных'
                if calculated_params and calculated_params.evaporation_ratio > float(i.limit_hi):
                    recommendations['Коэффициент упаривания Водоблок/УГОВ'] = i.recommendation2
                elif calculated_params and calculated_params.evaporation_ratio < float(i.limit_lo):
                    recommendations['Коэффициент упаривания Водоблок/УГОВ'] = i.recommendation1
                else:
                    recommendations['no_recom'] = 'В пределах нормы'
            if 'Транспорт кальциевой жесткости' in i.title:
                if not calculated_params:
                    recommendations['no_data'] = 'Нет данных'
                if calculated_params and calculated_params.calcium_hardness_transport > float(i.limit_hi):
                    recommendations['Транспорт кальциевой жесткости'] = i.recommendation2
                elif calculated_params and calculated_params and calculated_params.calcium_hardness_transport < float(i.limit_lo):
                    recommendations['Транспорт кальциевой жесткости'] = i.recommendation1
                else:
                    recommendations['no_recom'] = 'В пределах нормы'
            if 'Объем продувки' in i.title:
                if not calculated_params:
                    recommendations['no_data'] = 'Нет данных'
                if calculated_params and calculated_params.purge_volume > float(i.limit_hi):
                    recommendations['Объем продувки'] = i.recommendation2
                elif calculated_params and calculated_params.purge_volume < float(i.limit_lo):
                    recommendations['Объем продувки'] = i.recommendation1
                else:
                    recommendations['no_recom'] = 'В пределах нормы'
            if 'Потери с испарением' in i.title:
                if not calculated_params:
                    recommendations['no_data'] = 'Нет данных'
                if calculated_params and calculated_params.evaporative_loss > float(i.limit_hi):
                    recommendations['Потери с испарением'] = i.recommendation2
                elif calculated_params and calculated_params.evaporative_loss < float(i.limit_lo):
                    recommendations['Потери с испарением'] = i.recommendation1
                else:
                    recommendations['no_recom'] = 'В пределах нормы'
            if 'Капельный унос' in i.title:
                if not calculated_params:
                    recommendations['no_data'] = 'Нет данных'
                if calculated_params and calculated_params.drip_loss > float(i.limit_hi):
                    recommendations['Капельный унос'] = i.recommendation2
                elif calculated_params and calculated_params.drip_loss < float(i.limit_lo):
                    recommendations['Капельный унос'] = i.recommendation1
                else:
                    recommendations['no_recom'] = 'В пределах нормы'
            if 'Несанкционированные потери' in i.title:
                if not calculated_params:
                    recommendations['no_data'] = 'Нет данных'
                if calculated_params and calculated_params.unauthorized_loss > float(i.limit_hi):
                    recommendations['Несанкционированные потери'] = i.recommendation2
                elif calculated_params and calculated_params.unauthorized_loss < float(i.limit_lo):
                    recommendations['Несанкционированные потери'] = i.recommendation1
                else:
                    recommendations['no_recom'] = 'В пределах нормы'
        return recommendations
