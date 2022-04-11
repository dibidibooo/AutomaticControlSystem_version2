from django.contrib.auth.models import User, Group
from rest_framework import serializers

from accounts.models import Profile
from projects.models import TaskAssign, ComponentsSite1, ComponentsSite2, ComponentsSite3


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
        fields = ['first_name', 'last_name', 'email', 'profile']


class TasksSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TaskAssign
        fields = ['id', 'task', 'user', 'start_date', 'deadline', 'comp_title', 'sampling_site', 'plant_unit', 'status']


class Results1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentsSite1
        fields = '__all__'


class Results2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentsSite2
        fields = '__all__'


class Results3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentsSite3
        fields = '__all__'
