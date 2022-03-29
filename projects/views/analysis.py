from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.views.tasks import TaskCreate

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
    Component,
    TaskAssign,
)
from projects.multiforms import MultiFormsView


class AnalysisCreateView(MultiFormsView):
    template_name = "projects/projectsgrid_test.html"
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
                    }

    success_url = reverse_lazy('projects-createview')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Загрузка анализов'
        context['pageview'] = 'Projects'
        context['components'] = Component.objects.all()
        context['tasks'] = TaskAssign.objects.all()
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
        task_create.site1_task(form)
        return HttpResponseRedirect(self.success_url)

    # Водоблок - 2 | Установка АВТ напротив погружного холодильника №42
    def site2_form_valid(self, form):
        print(self.request.GET)
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
        task_create.site2_task(form)
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
            water_type_id=1
        )
        task_create = TaskCreate()
        task_create.site3_task(form)
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
            water_type_id=self.request.POST.get('water_type')
        )
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
            water_type_id=1
        )
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
            water_type_id=1
        )
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
            water_type_id=1
        )
        return HttpResponseRedirect(self.success_url)


class ProjectsListView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'heading': "Projects List",
            'pageview': "Projects"
        }
        return render(request, 'projects/projectslist.html', context)


class ProjectOverviewView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'heading': "Таблица",
            'pageview': "Projects"
        }
        return render(request, 'projects/projectsoverview.html', context)


class ResultsView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = TaskAssign.objects.all()
        components = Component.objects.all()
        results_site1 = self.get_results1()
        results_site2 = self.get_results2()
        results_site3 = self.get_results3()
        results_site4 = self.get_results4()
        results_site5 = self.get_results5()
        results_site6 = self.get_results6()
        results_site7 = self.get_results7()
        results_site8 = self.get_results8()
        results_site9 = self.get_results9()
        results_site10 = self.get_results10()
        results_site11 = self.get_results11()
        results_site12 = self.get_results12()
        results_site13 = self.get_results13()
        results_site14 = self.get_results14()
        context = {
            'heading': "Результаты",
            'pageview': "Projects",
            'components': components,
            'tasks': tasks,
            'results1': results_site1,
            'results2': results_site2,
            'results3': results_site3,
            'results4': results_site4,
            'results5': results_site5,
            'results6': results_site6,
            'results7': results_site7,
            'results8': results_site8,
            'results9': results_site9,
            'results10': results_site10,
            'results11': results_site11,
            'results12': results_site12,
            'results13': results_site13,
            'results14': results_site14,
        }
        return render(request, 'projects/createnew.html', context)

    def get_results1(self):
        results_site = {}
        tasks = TaskAssign.objects.all()
        try:
            sample = ComponentsSite1.objects.all().latest('datetime')
            for task in tasks:
                if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                    results_site[task.comp_title] = task.task.title
                else:
                    results_site['no_recom'] = 'Рекомендация не требуется'
            for key, value in ComponentsSite1.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite1.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results2(self):
        results_site = {}
        tasks = TaskAssign.objects.all()
        try:
            sample = ComponentsSite2.objects.all().latest('datetime')
            for task in tasks:
                if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                    results_site[task.comp_title] = task.task.title
                else:
                    results_site['no_recom'] = 'Рекомендация не требуется'
            for key, value in ComponentsSite2.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite2.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results3(self):
        results_site = {}
        tasks = TaskAssign.objects.all()
        try:
            sample = ComponentsSite3.objects.all().latest('datetime')
            for task in tasks:
                if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                    results_site[task.comp_title] = task.task.title
                else:
                    results_site['no_recom'] = 'Рекомендация не требуется'
            for key, value in ComponentsSite3.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite3.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results4(self):
        results_site = {}
        try:
            for key, value in ComponentsSite4.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite4.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results5(self):
        results_site = {}
        try:
            for key, value in ComponentsSite5.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite5.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results6(self):
        results_site = {}
        try:
            for key, value in ComponentsSite6.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results7(self):
        results_site = {}
        try:
            for key, value in ComponentsSite7.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results8(self):
        results_site = {}
        try:
            for key, value in ComponentsSite8.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results9(self):
        results_site = {}
        try:
            for key, value in ComponentsSite9.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results10(self):
        results_site = {}
        try:
            for key, value in ComponentsSite10.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results11(self):
        results_site = {}
        try:
            for key, value in ComponentsSite11.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results12(self):
        results_site = {}
        try:
            for key, value in ComponentsSite12.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results13(self):
        results_site = {}
        try:
            for key, value in ComponentsSite13.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site

    def get_results14(self):
        results_site = {}
        try:
            for key, value in ComponentsSite14.objects.values().latest('datetime').items():
                if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                    results_site[key] = value
        except ComponentsSite6.DoesNotExist:
            results_site['no_data'] = 'Нет данных'
        return results_site