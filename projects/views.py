from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ResultForm
from .models import (
    PlantUnit,
    SamplingSite,
    WaterType,
    Result,
    Sample,
    Component
)


class AnalysisCreateView(LoginRequiredMixin, CreateView):
    model = Result
    template_name = 'projects/projectsgrid_test.html'
    context_object_name = 'results'
    form_class = ResultForm
    success_url = reverse_lazy('projects-createview')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Загрузка анализов'
        context['pageview'] = 'Projects'
        context['components'] = Component.objects.all()
        return context

    def form_valid(self, form):
        result = form.save()
        components = Component.objects.all()
        for component in components:
            if result.component.pk == component.pk:
                pass
        # sample = Sample(result_id=result.pk, sampling_site_id=self.request.POST.get('plant_unit'))
        return super().form_valid(form)


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
        return render(request,'projects/projectsoverview.html', context)


class ResultsView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'heading': "Результаты",
            'pageview': "Projects"
        }
        return render(request, 'projects/createnew.html', context)
