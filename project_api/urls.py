from django.urls import path, include
from rest_framework import routers

from project_api.views import (
    TaskViewSet,
    Results1ViewSet,
    Results2ViewSet,
    Results3ViewSet,
    UserViewSet, get_results1
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
    path('get_results1', get_results1)
]
