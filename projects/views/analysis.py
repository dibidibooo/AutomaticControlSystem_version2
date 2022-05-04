from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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
    Site16Form, AdditionalAnalysisForm,
)
from projects.models import (
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
    Component, AdditionalComponents, PlantUnit,
)
from projects.multiforms import MultiFormsView


class AnalysisCreateView(PermissionRequiredMixin, MultiFormsView):
    permission_required = ('projects.add_componentssite1',)
    template_name = "projects/analyses_create.html"
    form_classes = {'site1': Site1Form,
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

        ComponentsSite1.objects.create(
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
            sampling_site_id=1,
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site1_task(form, 1)
        return HttpResponseRedirect(self.success_url)

    # Водоблок - 2 | Установка АВТ напротив погружного холодильника №42
    def site2_form_valid(self, form):
        oil_prod = form.cleaned_data.get('oil_prod')
        ph = form.cleaned_data.get('ph')
        suspended_solids = form.cleaned_data.get('suspended_solids')
        form_name = form.cleaned_data.get('action')

        ComponentsSite2.objects.create(
            oil_prod=oil_prod,
            ph=ph,
            suspended_solids=suspended_solids,
            sampling_site_id=2,
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site2_task(form, 1)
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

        ComponentsSite3.objects.create(
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
            sampling_site_id=3,
            water_type_id=2
        )
        task_create = TaskCreate()
        task_create.site3_task(form, 1)
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

        ComponentsSite4.objects.create(
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
            sampling_site_id=4,
            water_type_id=2
        )
        task_create = TaskCreate()
        task_create.site4_task(form, 2)
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

        ComponentsSite5.objects.create(
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
            sampling_site_id=5,
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site5_task(form, 1)
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

        ComponentsSite6.objects.create(
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
            sampling_site_id=6,
            water_type_id=water_type
        )
        task_create = TaskCreate()
        task_create.site6_task(form, water_type)
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

        ComponentsSite7.objects.create(
            suspended_solids=suspended_solids,
            chlorides=chlorides,
            sulfates=sulfates,
            ph=ph,
            alkalinity=alkalinity,
            hardness_calcium=hardness_calcium,
            hardness=hardness,
            iron=iron,
            sampling_site_id=7,
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site7_task(form, 1)
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

        ComponentsSite8.objects.create(
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
            sampling_site_id=8,
            water_type_id=2
        )
        task_create = TaskCreate()
        task_create.site8_task(form, 2)
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

        ComponentsSite9.objects.create(
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
            sampling_site_id=9,
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site9_task(form, 1)
        return HttpResponseRedirect(self.success_url)

    # УГОВ | Подача на градирню в районе 77-ТI-205 77-SN-007
    def site10_form_valid(self, form):
        chlorine = form.cleaned_data.get('chlorine')
        oil_prod = form.cleaned_data.get('oil_prod')
        salt = form.cleaned_data.get('salt')
        form_name = form.cleaned_data.get('action')

        ComponentsSite10.objects.create(
            chlorine=chlorine,
            oil_prod=oil_prod,
            salt=salt,
            sampling_site_id=10,
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site10_task(form, 1)
        return HttpResponseRedirect(self.success_url)

    # УГОВ | На выходе с бокового фильтра 77-Z-003, 77-SN-008
    def site11_form_valid(self, form):
        suspended_solids = form.cleaned_data.get('suspended_solids')
        form_name = form.cleaned_data.get('action')

        ComponentsSite11.objects.create(
            suspended_solids=suspended_solids,
            sampling_site_id=11,
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site11_task(form, 1)
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

        ComponentsSite12.objects.create(
            oil_prod=oil_prod,
            suspended_subst=suspended_subst,
            ph=ph,
            oxygen_chem=oxygen_chem,
            active_subst=active_subst,
            ammonium=ammonium,
            sampling_site_id=12,
            water_type_id=3
        )
        task_create = TaskCreate()
        task_create.site12_task(form, 1)
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

        ComponentsSite13.objects.create(
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
            sampling_site_id=13,
            water_type_id=3
        )
        task_create = TaskCreate()
        task_create.site13_task(form, 1)
        return HttpResponseRedirect(self.success_url)

    # БОС -> Сточная вода после биологических очистных сооружений А1–SN-009
    def site14_form_valid(self, form):
        alkalinity = form.cleaned_data.get('alkalinity')
        hardness = form.cleaned_data.get('hardness')
        oxidability = form.cleaned_data.get('oxidability')
        salt = form.cleaned_data.get('salt')
        chlorine = form.cleaned_data.get('chlorine')
        form_name = form.cleaned_data.get('action')

        ComponentsSite14.objects.create(
            alkalinity=alkalinity,
            hardness=hardness,
            oxidability=oxidability,
            salt=salt,
            chlorine=chlorine,
            sampling_site_id=14,
            water_type_id=3
        )
        task_create = TaskCreate()
        task_create.site14_task(form, 1)
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

        ComponentsSite15.objects.create(
            suspended_subst=suspended_subst,
            oil_prod=oil_prod,
            oxygen_chem=oxygen_chem,
            ammonium=ammonium,
            phosphorus=phosphorus,
            oxygen_bio=oxygen_bio,
            sampling_site_id=15,
            water_type_id=3
        )
        task_create = TaskCreate()
        task_create.site15_task(form, 1)
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

        ComponentsSite16.objects.create(
            suspended_subst=suspended_subst,
            oil_prod=oil_prod,
            oxygen_chem=oxygen_chem,
            ammonium=ammonium,
            phosphorus=phosphorus,
            oxygen_bio=oxygen_bio,
            sampling_site_id=16,
            water_type_id=3
        )
        task_create = TaskCreate()
        task_create.site16_task(form, 1)
        return HttpResponseRedirect(self.success_url)


class AdditionalAnalysisCreateView(PermissionRequiredMixin, CreateView):
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
        return super().form_valid(form)


class ExcelTableView(PermissionRequiredMixin, View):
    permission_required = ['projects.view_task']

    def get(self, request):
        context = {
            'heading': "Таблица",
            'pageview': "Анализы",
            'tasks': Task.objects.order_by('start_date'),
            'site1': ComponentsSite1.objects.order_by('datetime'),
            'site2': ComponentsSite2.objects.order_by('datetime'),
            'site3': ComponentsSite3.objects.order_by('datetime'),
            'site4': ComponentsSite4.objects.order_by('datetime'),
            'site5': ComponentsSite5.objects.order_by('datetime'),
            'site6': ComponentsSite6.objects.order_by('datetime'),
            'site7': ComponentsSite7.objects.order_by('datetime'),
            'site8': ComponentsSite8.objects.order_by('datetime'),
            'site9': ComponentsSite9.objects.order_by('datetime'),
            'site10': ComponentsSite10.objects.order_by('datetime'),
            'site11': ComponentsSite11.objects.order_by('datetime'),
            'site12': ComponentsSite12.objects.order_by('datetime'),
            'site13': ComponentsSite13.objects.order_by('datetime'),
            'site14': ComponentsSite14.objects.order_by('datetime'),
            'site15': ComponentsSite15.objects.order_by('datetime'),
            'site16': ComponentsSite16.objects.order_by('datetime'),
        }
        return render(request, 'projects/excel_table.html', context)


class ResultsView(PermissionRequiredMixin, View):
    permission_required = 'projects.view_componentssite1'

    def get(self, request):
        tasks = Task.objects.all()
        components = Component.objects.all()

        context = {
            'heading': "Результаты",
            'pageview': "Анализы",
            'components': components,
            'tasks': tasks,
            'results1': self.get_results1(),
            'results2': self.get_results2(),
            'results3': self.get_results3(),
            'results4': self.get_results4(),
            'results5': self.get_results5(),
            'results6': self.get_results6(),
            'results6_2': self.get_results6_2(),
            'results7': self.get_results7(),
            'results8': self.get_results8(),
            'results9': self.get_results9(),
            'results10': self.get_results10(),
            'results11': self.get_results11(),
            'results12': self.get_results12(),
            'results13': self.get_results13(),
            'results14': self.get_results14(),
            'results15': self.get_results15(),
            'results16': self.get_results16(),
            'res_additional_1': self.get_add_results1(),
            'res_additional_2': self.get_add_results2(),
            'res_additional_3': self.get_add_results3(),
            'res_additional_4': self.get_add_results4(),
            'res_additional_5': self.get_add_results5(),
            'res_additional_6': self.get_add_results6(),
        }

        # Сравнение показателей с оборотной воды и с подпиточной воды
        dict1 = {}
        dict2 = {}
        a = ComponentsSite6.objects.filter(water_type_id=1).values().latest('datetime')
        b = ComponentsSite6.objects.filter(water_type_id=2).values().latest('datetime')
        for k, v in a.items():
            if k != 'id' and k != 'datetime' and k != 'sampling_site_id' and k != 'water_type_id':
                dict1[k] = v
        for k, v in b.items():
            if k != 'id' and k != 'datetime' and k != 'sampling_site_id' and k != 'water_type_id':
                dict2[k] = v

        diffkeys = [k for k in dict1 if dict1[k] < dict2[k]]
        if diffkeys:
            context['unit_3_warning'] = """
            Показатели компонентов БОВ-2 с оборотной воды ниже показателей с подпиточной воды.
            Пожалуйста, обратите внимание!
            """
        return render(request, 'projects/analyses_results.html', context)

    def get_add_results1(self):
        if AdditionalComponents.objects.filter(plant_unit_id=1):
            return AdditionalComponents.objects.filter(plant_unit_id=1).latest('datetime')

    def get_add_results2(self):
        if AdditionalComponents.objects.filter(plant_unit_id=2):
            return AdditionalComponents.objects.filter(plant_unit_id=2).latest('datetime')

    def get_add_results3(self):
        if AdditionalComponents.objects.filter(plant_unit_id=3):
            return AdditionalComponents.objects.filter(plant_unit_id=3).latest('datetime')

    def get_add_results4(self):
        if AdditionalComponents.objects.filter(plant_unit_id=4):
            return AdditionalComponents.objects.filter(plant_unit_id=4).latest('datetime')

    def get_add_results5(self):
        if AdditionalComponents.objects.filter(plant_unit_id=5):
            return AdditionalComponents.objects.filter(plant_unit_id=5).latest('datetime')

    def get_add_results6(self):
        if AdditionalComponents.objects.filter(plant_unit_id=6):
            return AdditionalComponents.objects.filter(plant_unit_id=6).latest('datetime')

    def get_results1(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite1.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 1 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite1.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite1.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results2(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite2.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 2 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite2.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite2.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results3(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite3.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 3 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite3.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite3.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results4(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite4.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 4 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite4.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite4.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results5(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite5.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 5 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite5.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite5.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results6(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite6.objects.filter(water_type_id=1).latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 6 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite6.objects.filter(water_type_id=1).values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results6_2(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite6.objects.filter(water_type_id=2).latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 6 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite6.objects.filter(water_type_id=2).values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results7(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite7.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 7 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M') == task.start_date.strftime('%Y-%m-%d %H:%M')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite7.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite7.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results8(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite8.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 8 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite8.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite8.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results9(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite9.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 9 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite9.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite9.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results10(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite10.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 10 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite10.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite10.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results11(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite11.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 11 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite11.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite11.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results12(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite12.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 12 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite12.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite12.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results13(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite13.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 13 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite13.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite13.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results14(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite14.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 14 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite14.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite14.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results15(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite15.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 15 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite15.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite15.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results16(self):
        results_site = {}
        tasks = Task.objects.all()
        try:
            sample = ComponentsSite16.objects.all().latest('datetime')
            for task in tasks:
                if sample.sampling_site_id == 16 and (
                        sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S')
                ):
                    results_site[task.comp_title] = task.title
                else:
                    results_site['no_recom'] = 'В пределах нормы'
            for key, value in ComponentsSite16.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite16.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site