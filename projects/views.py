from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProjectsGridView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading':"Загрузка анализов",
            'pageview': "Projects"
        }
        return render (request,'projects/projectsgrid.html',context)

class ProjectsListView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading':"Projects List",
            'pageview': "Projects"
        }
        return render (request,'projects/projectslist.html',context)

class ProjectOverviewView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading':"Таблица",
            'pageview': "Projects"
        }
        return render (request,'projects/projectsoverview.html',context)

class CreateViewView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading':"Результаты",
            'pageview': "Projects"
        }
        return render (request,'projects/createnew.html',context)
