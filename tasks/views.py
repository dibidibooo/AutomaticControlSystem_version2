from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class KanbanBoardView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading': "Kanban Board",
            'pageview': "Tasks"
        }
        return render (request,'tasks/kanbanboard.html',context)

class TaskListView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading': "Task List",
            'pageview': "Tasks"
        }
        return render (request,'tasks/tasklist.html',context)

class CreateTaskView(LoginRequiredMixin,View):
    def get(self , request):
        context = {
            'heading': "Create Task",
            'pageview': "Tasks"
        }
        return render (request,'tasks/createtask.html',context)