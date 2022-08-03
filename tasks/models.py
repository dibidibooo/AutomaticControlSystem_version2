from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from django.db import models
from django.template import loader
from model_utils import FieldTracker

from accounts.models import Profile
from projects.helpers import send_html_mail


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Задача')
    user = models.ForeignKey(get_user_model(), related_name='task_assignee', null=True, blank=True,
                             on_delete=models.PROTECT, verbose_name='Исполнитель')
    responsible = models.ForeignKey(Group, related_name='task_responsible',
                                    on_delete=models.CASCADE, verbose_name='Ответственный')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата назначения задачи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения задачи')
    completion_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата и время выполнения задачи')
    comp_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название компонента')
    comp_value = models.IntegerField(verbose_name='Показатель компонента')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='task')
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
    tracker = FieldTracker(fields=['user_id', 'deadline', 'status_id', ])

    def save(self, *args, **kwargs):
        # Отправка email уведомлений при создании задач
        from_email = settings.EMAIL_HOST_USER
        val = {
            'task_title': self.title,
            'component': self.comp_title,
            'sampling_site': self.sampling_site,
            'plant_unit': self.plant_unit,
        }
        html_message = loader.render_to_string('emails/task_create.html', val)
        to_email = list()
        for responsible in User.objects.filter(groups__name=self.responsible):
            to_email.append(responsible.email)

        profiles = Profile.objects.all()
        for profile in profiles:
            if profile.position == 'Заместитель начальника цеха ОВиВ':
                to_email.append(profile.user.email)
            if profile.position == 'Инженер-технолог':
                to_email.append(profile.user.email)

        subject = f'Назначена новая задача'

        if self.pk is None:
            send_html_mail(subject=subject, html_content=html_message, recipient_list=to_email, sender=from_email)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Задача №{self.pk}'


class Comment(models.Model):
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
    text = models.TextField(max_length=2000, verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Дата изменения")

    def save(self, *args, **kwargs):
        from_email = settings.EMAIL_HOST_USER
        val = {
            'task_id': self.task.id,
            'task_title': self.task.title,
            'component': self.task.comp_title,
            'sampling_site': self.task.sampling_site,
            'plant_unit': self.task.plant_unit,
            'author': self.author,
            'text': self.text
        }
        html_message = loader.render_to_string('emails/comment_create.html', val)

        to_email = list()
        if self.task.user:
            to_email.append(self.task.user.email)
        for responsible in User.objects.filter(groups__name=self.task.responsible):
            to_email.append(responsible.email)

        subject = f'Новый комментарий в задаче #{self.task.id}'

        if to_email and self.pk is None:
            send_html_mail(subject=subject, html_content=html_message, recipient_list=to_email, sender=from_email)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name_plural = 'Comments'


class ChangesTracker(models.Model):
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name="changes")
    text = models.CharField(max_length=200, verbose_name='Текст изменения')
    who_changed = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Кто изменил')
    changed_to = models.CharField(max_length=200, verbose_name='На что изменил')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    failure_reason = models.CharField(max_length=300, null=True, blank=True, verbose_name='Причина невыполнения задачи')
