from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile',
                                on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name='Должность')
    role = models.ForeignKey(Group, related_name='profile', null=True, blank=True,
                             on_delete=models.CASCADE, verbose_name='Роль пользователя')

    def __str__(self):
        return self.user.get_full_name() + "'s profile"
