from django.urls import path
from .views.analysis import AnalysisCreateView, AdditionalAnalysisCreateView, ProjectOverviewView, ResultsView

urlpatterns = [
    path('analyzes', AnalysisCreateView.as_view(), name='analyzes_create'),
    path('analyzes/additional', AdditionalAnalysisCreateView.as_view(), name='additional_analyzes_create'),
    path('table', ProjectOverviewView.as_view(), name='excel_table'),
    path('results', ResultsView.as_view(), name='analyzes_results'),
]
