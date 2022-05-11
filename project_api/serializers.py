from django.contrib.auth.models import User, Group
from rest_framework import serializers

from accounts.models import Profile
from projects.models import (
    SamplingSite,
    PlantUnit,
    Status,
    # ComponentsSite1,
    # ComponentsSite2,
    # ComponentsSite3,
    ComponentsSite,
    Component,
)
from tasks.models import Task


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class ProfileSerializer(serializers.ModelSerializer):
    role = GroupSerializer()

    class Meta:
        model = Profile
        fields = ['phone', 'position', 'role']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'profile']


class SamplingSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamplingSite
        fields = '__all__'


class PlantUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantUnit
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    sampling_site = SamplingSiteSerializer()
    plant_unit = PlantUnitSerializer()
    status = StatusSerializer()

    class Meta:
        model = Task
        fields = ['id', 'title', 'user', 'start_date', 'deadline',
                  'comp_title', 'sampling_site', 'plant_unit', 'status']


class Results1Serializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = ComponentsSite
        fields = ['data']

    def get_data(self):
        data_dict = {}
        for i in ComponentsSite.objects.values():
            for key, value in i.items():
                data_dict.setdefault(key, []).append(value)
        return data_dict


# class Results2Serializer(serializers.ModelSerializer):
#     data = serializers.SerializerMethodField()
#
#     class Meta:
#         model = ComponentsSite2
#         fields = ['id', 'data']
#
#     def get_data(self, comp_site):
#         data_dict = {}
#         for i in ComponentsSite2.objects.values():
#             for key, value in i.items():
#                 if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
#                     data_dict[key] = value
#         return data_dict
#
#
# class Results3Serializer(serializers.ModelSerializer):
#     data = serializers.SerializerMethodField()
#
#     class Meta:
#         model = ComponentsSite3
#         fields = ['id', 'data']
#
#     def get_data(self, comp_site):
#         data_dict = {}
#         for i in ComponentsSite3.objects.values():
#             for key, value in i.items():
#                 if key != 'id' and key != 'datetime' and key != 'sampling_site_id' and key != 'water_type_id':
#                     data_dict[key] = value
#         return data_dict
