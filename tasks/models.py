# from adminsortable.fields import SortableForeignKey
# from adminsortable.models import SortableMixin
# from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Задача')
    user = models.ForeignKey(get_user_model(), related_name='task_assign', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата назначения задачи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения задачи')
    completion_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время выполнения задачи')
    comp_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название компонента')
    sampling_site = models.ForeignKey(
        'projects.SamplingSite',
        null=True,
        blank=True,
        related_name='task_assign',
        on_delete=models.CASCADE,
        verbose_name='Место отбора проб'
    )
    plant_unit = models.ForeignKey(
        'projects.PlantUnit',
        related_name='task_assign',
        on_delete=models.CASCADE,
        verbose_name='Установка'
    )
    notification = models.ForeignKey(
        'projects.Notification',
        related_name='task_assign',
        on_delete=models.CASCADE,
        verbose_name='Уведомление'
    )
    status = models.ForeignKey('projects.Status', related_name='task_assign', on_delete=models.CASCADE, default=1)


class Comment(models.Model):
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
    text = models.TextField(max_length=2000, verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name_plural = 'Comments'
