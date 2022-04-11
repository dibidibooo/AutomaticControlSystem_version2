from django.urls import path, include
from rest_framework import routers

from project_api.views import (
    get_results1,
    get_results2,
    get_results3,
    get_results4,
    get_results5,
    get_results6,
    get_results7,
    get_results8,
    get_results9,
    get_results10,
    get_results11,
    get_results12,
    get_results13,
    get_results14, TaskViewSet, Results1ViewSet, Results2ViewSet, Results3ViewSet
)

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'results1', Results1ViewSet)
router.register(r'results2', Results2ViewSet)
router.register(r'results3', Results3ViewSet)

urlpatterns = [
    path('results1', get_results1, name='results1'),
    path('results2', get_results2, name='results2'),
    path('results3', get_results3, name='results3'),
    path('results4', get_results4, name='results4'),
    path('results5', get_results5, name='results5'),
    path('results6', get_results6, name='results6'),
    path('results7', get_results7, name='results7'),
    path('results8', get_results8, name='results8'),
    path('results9', get_results9, name='results9'),
    path('results10', get_results10, name='results10'),
    path('results11', get_results11, name='results11'),
    path('results12', get_results12, name='results12'),
    path('results13', get_results13, name='results13'),
    path('results14', get_results14, name='results14'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
