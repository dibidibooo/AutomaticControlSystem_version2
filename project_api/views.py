from django.http import JsonResponse
from rest_framework import viewsets

from project_api.serializers import TasksSerializer, Results1Serializer, Results2Serializer, Results3Serializer
from projects.models import (
    TaskAssign,
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
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskAssign.objects.all()
    serializer_class = TasksSerializer


class Results1ViewSet(viewsets.ModelViewSet):
    queryset = ComponentsSite1.objects.all()
    serializer_class = Results1Serializer


class Results2ViewSet(viewsets.ModelViewSet):
    queryset = ComponentsSite2.objects.all()
    serializer_class = Results2Serializer


class Results3ViewSet(viewsets.ModelViewSet):
    queryset = ComponentsSite3.objects.all()
    serializer_class = Results3Serializer


def get_results1(request):
    results_site = {}
    for key, value in ComponentsSite1.objects.values().latest('oil_prod').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results2(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite2.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite2.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite2.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results3(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite3.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite3.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite3.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results4(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite4.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite4.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite4.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results5(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite5.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite5.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite5.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results6(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite6.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite6.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite6.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results7(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite7.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite7.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite7.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results8(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite8.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite8.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite8.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results9(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite9.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite9.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite9.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results10(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite10.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite10.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite10.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results11(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite11.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite11.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite11.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results12(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite12.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite12.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite12.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results13(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite13.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite13.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite13.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})

def get_results14(request):
    results_site = {}
    tasks = TaskAssign.objects.all()
    try:
        sample = ComponentsSite14.objects.all().latest('datetime')
        for task in tasks:
            if sample.datetime.strftime('%Y-%m-%d %H:%M:%S') == task.start_date.strftime('%Y-%m-%d %H:%M:%S'):
                results_site[task.comp_title] = task.task.capitalize()
            else:
                results_site['no_recom'] = 'В пределах нормы'
        for key, value in ComponentsSite14.objects.values().latest('datetime').items():
            if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
                results_site[key] = value
    except ComponentsSite14.DoesNotExist:
        results_site['no_data'] = 'Нет данных'
    return JsonResponse(results_site, json_dumps_params={'ensure_ascii': False})
