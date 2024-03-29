from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView

from tasks.models import Task
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
    AdditionalCalculations
)
from projects.multiforms import MultiFormsView


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
            water_type_id=water_type
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site2_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site3_task(form, water_type, responsible_id=4)
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
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site4_task(form, water_type, responsible_id=4)
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
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site5_task(form, water_type, responsible_id=4)
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
        form_name = form.cleaned_data.get('action')
        water_type = self.request.POST.get('water_type')
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
            plant_unit_id=self.request.POST['plant_unit'],
            sampling_site_id=smpl_site,
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site6_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site7_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site8_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site9_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site10_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site11_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site12_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site13_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site14_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site15_task(form, water_type, responsible_id=4)
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
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site16_task(form, water_type, responsible_id=4)
        return HttpResponseRedirect(self.success_url)


class AdditionalAnalysisCreateView(PermissionRequiredMixin, CreateView):
    """Загрузка ежедневных анализов"""

    model = AdditionalComponents
    form_class = AdditionalAnalysisForm
    template_name = 'projects/additional_analyses_create.html'
    success_url = reverse_lazy('analyzes_results')
    permission_required = ['add_additionalcomponents']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Загрузка ежедневных анализов"
        context['pageview'] = "Анализы"
        context['plant_units'] = PlantUnit.objects.all()
        return context

    def form_valid(self, form):
        unit_id = self.request.POST.get('uid')
        unit = get_object_or_404(PlantUnit, pk=unit_id)
        form.instance.plant_unit = unit
        form.save()
        if int(unit_id) in range(5, 7):
            formula = AdditionalCalc()
            formula.calculations(unit=int(unit_id))
        return super().form_valid(form)


class AdditionalCalc:
    """Дополнительные расчеты по формулам"""

    def calculations(self, unit: int) -> None:
        smpl_site_recycled = self.sampling_site_recycled_water(unit)
        smpl_site_running = self.sampling_site_running_water(unit)

        # Коэффициент упаривания
        if smpl_site_recycled == 6 and smpl_site_running == 6:
            chlorides_recycled_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_recycled, plant_unit_id=unit, water_type_id=1).last().chlorides
            chlorides_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running, plant_unit_id=unit, water_type_id=2).last().chlorides
        else:
            chlorides_recycled_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_recycled, plant_unit_id=unit).last().chlorides
            chlorides_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running, plant_unit_id=unit).last().chlorides
        evaporation_ratio = chlorides_recycled_water / chlorides_running_water
        evaporation_ratio = round(evaporation_ratio, 3)

        # Транспорт кальциевой жесткости
        if smpl_site_recycled == 6 and smpl_site_running == 6:
            calcium_recycled_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_recycled, plant_unit_id=unit, water_type_id=1).last().hardness_calcium
            calcium_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running, plant_unit_id=unit, water_type_id=2).last().hardness_calcium
        else:
            calcium_recycled_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_recycled, plant_unit_id=unit).last().hardness_calcium
            calcium_running_water = ComponentsSite.objects.filter(
                sampling_site_id=smpl_site_running, plant_unit_id=unit).last().hardness_calcium
        tr_ca = (calcium_recycled_water * 100) / (calcium_running_water * evaporation_ratio)
        tr_ca = round(tr_ca, 3)

        # Объем продувки
        running_water_consumption = AdditionalComponents.objects.all().last().running_water_consumption
        p3 = running_water_consumption / evaporation_ratio
        p3 = round(p3, 3)

        # Потери с испарением
        hot_water_temp = AdditionalComponents.objects.all().last().hot_water_temp
        cold_water_temp = AdditionalComponents.objects.all().last().cold_water_temp
        delta_temp = hot_water_temp - cold_water_temp

        k = 0
        today = datetime.today()
        if today.month in range(6, 9):
            k = 1
        elif today.month in range(1, 3) or today.month == 12:
            k = 0.5
        elif today.month in range(3, 6) or today.month in range(9, 12):
            k = 0.75

        x = (delta_temp * k) / 100
        recycled_water_consumption = AdditionalComponents.objects.all().last().recycled_water_consumption
        p1 = x * recycled_water_consumption
        p1 = round(p1, 3)

        # Капельный унос
        p2 = recycled_water_consumption * 0.002
        p2 = round(p2, 3)

        # Несанкционированные потери
        unauthorized_loss = running_water_consumption - p1 - p2 - p3
        unauthorized_loss = round(unauthorized_loss, 3)

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
    def sampling_site_recycled_water(unit: int) -> int:
        smpl_site_recycled = 0
        if unit == 1:
            smpl_site_recycled = 1
        elif unit == 2:
            smpl_site_recycled = 5
        elif unit == 3:
            smpl_site_recycled = 6
        elif unit == 4:
            smpl_site_recycled = 8
        return smpl_site_recycled

    @staticmethod
    def sampling_site_running_water(unit: int) -> int:
        smpl_site_running = 0
        if unit == 1:
            smpl_site_running = 3
        elif unit == 2:
            smpl_site_running = 4
        elif unit == 3:
            smpl_site_running = 6
        elif unit == 4:
            smpl_site_running = 9
        return smpl_site_running


class ExcelTableView(PermissionRequiredMixin, View):
    permission_required = ['projects.view_task']

    def get(self, request):
        context = {
            'heading': "Таблица",
            'pageview': "Анализы",
            'tasks': Task.objects.order_by('start_date'),
            'results': ComponentsSite.objects.order_by('datetime'),
        }
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
            'results6': self.get_results_2(6, 1),
            'results6_2': self.get_results_2(6, 2),
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
            'additional_formula1': AdditionalCalculations.objects.filter(plant_unit_id=1).last(),
            'additional_formula2': AdditionalCalculations.objects.filter(plant_unit_id=2).last(),
            'additional_formula3': AdditionalCalculations.objects.filter(plant_unit_id=3).last(),
            'additional_formula4': AdditionalCalculations.objects.filter(plant_unit_id=4).last(),
        }

        # Сравнение показателей с оборотной воды и с подпиточной воды на БОВ-2
        if self.unit3_results_comparison() is not None:
            context['unit_3_warning'] = self.unit3_results_comparison()

        return render(request, 'projects/analyses_results.html', context)

    @staticmethod
    def unit3_results_comparison():
        dict1 = {}
        dict2 = {}
        if ComponentsSite.objects.filter(sampling_site_id=6, water_type_id=1) and \
                ComponentsSite.objects.filter(sampling_site_id=6, water_type_id=2):

            a = ComponentsSite.objects.filter(sampling_site_id=6, water_type_id=1).values().latest('datetime')
            b = ComponentsSite.objects.filter(sampling_site_id=6, water_type_id=2).values().latest('datetime')
            for key, value in a.items():
                if value is not None and key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id' and key != 'plant_unit':
                    dict1[key] = value
            for key, value in b.items():
                if value is not None and key is not None and key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id' and key != 'plant_unit':
                    dict2[key] = value

        diffkeys = [key for key in dict1 if dict1[key] < dict2[key]]
        if diffkeys:
            return """
            Показатели компонентов БОВ-2 с оборотной воды ниже показателей с подпиточной воды.
            Пожалуйста, обратите внимание!
            """
        else:
            return None

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
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    @staticmethod
    def get_results_2(site_id: int, water_type_id: int) -> dict:
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite.objects.filter(
                sampling_site_id=site_id, water_type_id=water_type_id).latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 6 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite.objects.filter(
                    sampling_site_id=site_id, water_type_id=water_type_id).values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site
