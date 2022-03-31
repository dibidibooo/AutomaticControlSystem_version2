from django.urls import path
from .views.analysis import AnalysisCreateView, ProjectsListView, ProjectOverviewView, ResultsView
from .views.tasks import TaskUpdateView

urlpatterns = [
    path('analyzes', AnalysisCreateView.as_view(), name='projects-projectsgrid'),
    path('projectslist', ProjectsListView.as_view(), name='projects-projectslist'),
    path('projectoverview', ProjectOverviewView.as_view(), name='projects-projectoverview'),
    path('results', ResultsView.as_view(), name='projects-createview'),
]
