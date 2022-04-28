from django.urls import path
from .views.analysis import AnalysisCreateView, AdditionalAnalysisCreateView, ProjectOverviewView, ResultsView

urlpatterns = [
    path('analyzes', AnalysisCreateView.as_view(), name='projects-projectsgrid'),
    path('projectslist', AdditionalAnalysisCreateView.as_view(), name='projects-projectslist'),
    path('table', ProjectOverviewView.as_view(), name='projects-projectoverview'),
    path('results', ResultsView.as_view(), name='projects-createview'),

]
