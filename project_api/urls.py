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
    get_results14, TaskViewSet, Results1ViewSet, Results2ViewSet, Results3ViewSet, UserViewSet
)

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'results1', Results1ViewSet)
router.register(r'results2', Results2ViewSet)
router.register(r'results3', Results3ViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
