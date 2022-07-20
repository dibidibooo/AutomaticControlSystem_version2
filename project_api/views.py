# from datetime import datetime
import datetime, time
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets

from project_api.serializers import (
    TasksSerializer,
    Results1Serializer,
    # Results2Serializer,
    # Results3Serializer,
    UserSerializer,
    ComponentSerializer
)
from projects.models import (
    # ComponentsSite1,
    # ComponentsSite2,
    # ComponentsSite3,
    # ComponentsSite4,
    # ComponentsSite5,
    # ComponentsSite6,
    # ComponentsSite7,
    # ComponentsSite8,
    # ComponentsSite9,
    # ComponentsSite10,
    # ComponentsSite11,
    # ComponentsSite12,
    # ComponentsSite13,
    # ComponentsSite14,
    # ComponentsSite15,
    # ComponentsSite16,
    ComponentsSite,
    Component,
)
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class Results1ViewSet(viewsets.ModelViewSet):
    queryset = ComponentsSite.objects.all()
    serializer_class = Results1Serializer


def is_data(name):
    """
    filter not data fields
    """
    if name == "id" \
            or name == "datetime" \
            or name == "water_type" \
            or name == "sampling_site_id" \
            or name == "sampling_site":
        return False
    else:
        return True


def get_results1(request):
    """
    api:
        data = [
            {
                "object_index": 1,
                "values":[
                    {
                        "name": "oil_prod",
                        "values": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                    }
                ]
            },
        ]
    """
    data_dict = {
        "data": [
            # TODO: Прописать все с правильными Индексами
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=1).order_by("id"), 1),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=2).order_by("id"), 2),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=3).order_by("id"), 3),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=4).order_by("id"), 4),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=5).order_by("id"), 5),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=6, water_type_id=1).order_by("id"), 6),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=6, water_type_id=2).order_by("id"), 61),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=7).order_by("id"), 7),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=8).order_by("id"), 8),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=9).order_by("id"), 9),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=10).order_by("id"), 10),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=11).order_by("id"), 11),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=12).order_by("id"), 12),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=13).order_by("id"), 13),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=14).order_by("id"), 14),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=15).order_by("id"), 15),
            get_object_statistic(ComponentsSite.objects.filter(sampling_site_id=16).order_by("id"), 16),
        ]
    }
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})


def get_object_statistic(items, object_index):
    # Component
    _values = {}
    _date_values = {}
    # on components
    for item in items.values():
        # all values on component
        for key, value in item.items():
            if is_data(key):
                # for mini
                if key in _values:
                    _values[key].append(value)
                else:
                    _values[key] = [value, ]

                # for full
                if key in _date_values:
                    _date_values[key].append([item["datetime"], value])
                else:
                    _date_values[key] = [[item["datetime"], value], ]

    res = {
        "object_index": object_index,
        "values": [{"name": key, "values": _values[key]} for key in _values],
        "date_values": [{"name": key, "values": _date_values[key]} for key in _date_values],
    }
    return res
