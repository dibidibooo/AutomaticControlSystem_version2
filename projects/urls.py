from django.urls import path
from .views.analysis import AnalysisCreateView, ProjectsListView, ProjectOverviewView, ResultsView

urlpatterns = [
    path('projectsgrid', AnalysisCreateView.as_view(), name='projects-projectsgrid'),
    path('projectslist', ProjectsListView.as_view(), name='projects-projectslist'),
    path('projectoverview', ProjectOverviewView.as_view(), name='projects-projectoverview'),
    path('createview', ResultsView.as_view(), name='projects-createview'),
]
