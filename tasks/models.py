from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.template import loader
from model_utils import FieldTracker


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Задача')
    user = models.ForeignKey(get_user_model(), related_name='task_assignee', null=True, blank=True,
                             on_delete=models.PROTECT, verbose_name='Исполнитель')
    responsible = models.ForeignKey(get_user_model(), related_name='task_responsible',
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
        from_email = settings.EMAIL_HOST_USER
        val = {
            'task_title': self.title,
            'component': self.comp_title,
            'sampling_site': self.sampling_site,
            'plant_unit': self.plant_unit,
        }
        html_message = loader.render_to_string('emails/task_create.html', val)
        to_email = [self.responsible.email, ]
        subject = f'Назначена новая задача'
        body = f"""
        Добавлена новая задача '{self.title} для компонента {self.comp_title}'.
        (Место отбора проб: {self.sampling_site}. Установка: {self.plant_unit}.)

        Пройдите по ссылке, чтобы открыть доску задач: http://127.0.0.1:8000/tasks/kanbanboard
        """
        if self.pk is None:
            send_mail(subject, body, from_email,
                      to_email, fail_silently=False, html_message=html_message)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Задача № {self.pk}'


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
        to_email = [self.task.user.email, ]
        subject = f'Новый комментарий в задаче #{self.task.id}'
        body = f"""
        Добавлен новый комментарий в задаче #{self.task.id} - {self.task.title} для компонента {self.task.comp_title}.
        (Место отбора проб: {self.task.sampling_site}. Установка: {self.task.plant_unit}.)
        
        @{self.author}: '{self.text}.'
        
        Пройдите по ссылке, чтобы открыть доску задач: http://127.0.0.1:8000/tasks/kanbanboard
        """
        if self.pk is None:
            send_mail(subject, body, 'tussupbekov@gmail.com',
                      to_email, fail_silently=False, html_message=html_message)
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
