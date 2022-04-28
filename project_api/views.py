from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets

from project_api.serializers import (
    TasksSerializer,
    Results1Serializer,
    Results2Serializer,
    Results3Serializer,
    UserSerializer
)
from projects.models import (
    ComponentsSite1,
    ComponentsSite2,
    ComponentsSite3,
    ComponentsSite4,
    ComponentsSite5,
    ComponentsSite6,
    ComponentsSite7,
    ComponentsSite8,
    ComponentsSite9,
    ComponentsSite10,
    ComponentsSite11,
    ComponentsSite12,
    ComponentsSite13,
    ComponentsSite14,
    ComponentsSite15,
    ComponentsSite16,
)
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Results1ViewSet(viewsets.ModelViewSet):
    queryset = ComponentsSite1.objects.all()
    serializer_class = Results1Serializer


class Results2ViewSet(viewsets.ModelViewSet):
    queryset = ComponentsSite2.objects.all()
    serializer_class = Results2Serializer


class Results3ViewSet(viewsets.ModelViewSet):
    queryset = ComponentsSite3.objects.all()
    serializer_class = Results3Serializer

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
            get_object_statistic(ComponentsSite1.objects.all().order_by("id"), 1),
            get_object_statistic(ComponentsSite2.objects.all().order_by("id"), 2),
            get_object_statistic(ComponentsSite3.objects.all().order_by("id"), 3),
            get_object_statistic(ComponentsSite4.objects.all().order_by("id"), 4),

            get_object_statistic(ComponentsSite5.objects.all().order_by("id"), 5),

            get_object_statistic(ComponentsSite6.objects.filter(water_type_id=1).order_by("id"), 6),
            get_object_statistic(ComponentsSite6.objects.filter(water_type_id=2).order_by("id"), 61),
            get_object_statistic(ComponentsSite7.objects.all().order_by("id"), 7),
            get_object_statistic(ComponentsSite8.objects.all().order_by("id"), 8),

            get_object_statistic(ComponentsSite9.objects.all().order_by("id"), 9),

            get_object_statistic(ComponentsSite10.objects.all().order_by("id"), 10),
            get_object_statistic(ComponentsSite11.objects.all().order_by("id"), 11),
            get_object_statistic(ComponentsSite12.objects.all().order_by("id"), 12),
            get_object_statistic(ComponentsSite13.objects.all().order_by("id"), 13),
            get_object_statistic(ComponentsSite14.objects.all().order_by("id"), 14),
            get_object_statistic(ComponentsSite15.objects.all().order_by("id"), 15),
            get_object_statistic(ComponentsSite16.objects.all().order_by("id"), 16),
        ]
    }
    return JsonResponse(data_dict, json_dumps_params={'ensure_ascii': False})


def get_object_statistic(items, object_index):
    # Component
    _values = {}
    # on components
    for item in items.values():
        # all values on component
        for key, value in item.items():
            if is_data(key):
                if key in _values:
                    _values[key].append(value)
                else:
                    _values[key] = [value, ]

    res = {
        "object_index": object_index,
        "values": [{"name": key, "values": _values[key]} for key in  _values]
    }
    return res