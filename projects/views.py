from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import (
    ComponentsSite1,
    ComponentsSite2,
    ComponentsSite3,
    ComponentsSite4
)


class ProjectsGridView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'heading': "Загрузка анализов",
            'pageview': "Projects"
        }
        return render(request, 'projects/projectsgrid.html', context)


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


class CreateViewView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'heading': "Результаты",
            'pageview': "Projects"
        }
        return render(request,'projects/createnew.html', context)

    def post(self, request, *args, **kwargs):
        greeting = {}
        greeting['heading'] = "Create New Project"
        greeting['pageview'] = "Projects"
        site1 = ComponentsSite1
        site1.sampling_site.id
        site2 = ComponentsSite2
        site3 = ComponentsSite3
        site4 = ComponentsSite4
        return render(request, 'projects/projectsgrid_test.html', greeting)
