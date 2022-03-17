from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import Site1Form, Site2Form
from .models import (
    ComponentsSite1
)
from .multiforms import MultiFormsView


def form_redir(request):
    return render(request, 'pages/form_redirect.html')


def multiple_forms(request):
    if request.method == 'POST':
        site1_form = Site1Form(request.POST)
        site2_form = Site2Form(request.POST)
        if site1_form.is_valid() or site2_form.is_valid():
            print(777888)
            return HttpResponseRedirect(reverse('projects-createview'))
    else:
        site1_form = Site1Form()
        site2_form = Site2Form()

    return render(request, 'projects/multiple_forms.html', {
        'site1_form': site1_form,
        'site2_form': site2_form,
    })


class MultipleFormsDemoView(MultiFormsView):
    template_name = "projects/projectsgrid_test.html"
    form_classes = {'site1': Site1Form,
                    'site2': Site2Form,
                    }

    success_urls = {
        'site1': reverse_lazy('projects-createview'),
        'site2': reverse_lazy('projects-createview'),
    }

    def site1_form_valid(self, form):
        oil_prod = form.cleaned_data.get('oil_prod')
        suspended_subst = form.cleaned_data.get('suspended_subst')
        ph = form.cleaned_data.get('ph')
        oxygen_chem = form.cleaned_data.get('oxygen_chem')
        active_subst = form.cleaned_data.get('active_subst')
        ammonium = form.cleaned_data.get('ammonium')
        form_name = form.cleaned_data.get('action')
        ComponentsSite1.objects.create(
            oil_prod=oil_prod,
            suspended_subst=suspended_subst,
            ph=ph,
            oxygen_chem=oxygen_chem,
            active_subst=active_subst,
            ammonium=ammonium,
            sampling_site_id=1,
            water_type_id=1
        )
        return HttpResponseRedirect(self.get_success_url(form_name))

    def site2_form_valid(self, form):
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
        return HttpResponseRedirect(self.get_success_url(form_name))


# class AnalysisCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'projects/projectsgrid_test.html'
#     context_object_name = 'results'
#     success_url = reverse_lazy('projects-createview')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['heading'] = 'Загрузка анализов'
#         context['pageview'] = 'Projects'
#         context['components'] = Component.objects.all()
#         return context
#
#     def form_valid(self, form):
#         result = form.save()
#         components = Component.objects.all()
#         for component in components:
#             if result.component.pk == component.pk:
#                 pass
#         # sample = Sample(result_id=result.pk, sampling_site_id=self.request.POST.get('plant_unit'))
#         return super().form_valid(form)


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
