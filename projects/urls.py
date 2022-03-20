from django.urls import path
from projects import views

urlpatterns = [
    path('projectsgrid', views.AnalysisCreateView.as_view(), name='projects-projectsgrid'),
    path('projectslist', views.ProjectsListView.as_view(), name='projects-projectslist'),
    path('projectoverview', views.ProjectOverviewView.as_view(), name='projects-projectoverview'),
    path('createview', views.ResultsView.as_view(), name='projects-createview'),
]