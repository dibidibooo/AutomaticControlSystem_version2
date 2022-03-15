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
        greeting = {}
        greeting['heading'] = "Projects Grid"
        greeting['pageview'] = "Projects"
        return render(request, 'projects/projectsgrid.html', greeting)


class ProjectsListView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Projects List"
        greeting['pageview'] = "Projects"
        return render(request, 'projects/projectslist.html', greeting)


class ProjectOverviewView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Project Overview"
        greeting['pageview'] = "Projects"
        return render(request, 'projects/projectsoverview.html', greeting)


class CreateViewView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Create New Project"
        greeting['pageview'] = "Projects"
        return render(request, 'projects/projectsgrid_test.html', greeting)

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
