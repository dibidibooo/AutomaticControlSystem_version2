from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models import signals

from projects.models import Status
from .models import Task


@receiver(signals.post_save, sender=Task)
def send_task_send_email(sender, instance, created, **kwargs):
    task = Task.objects.get(id=instance.id)
    if not instance.user:
        print(f'{instance} has no assignee')
    elif instance.user and instance.user.email:
        subject = f'Изменения в задаче #{instance.id}'
        body = f'В задаче №{instance.id}:'
        if instance.tracker.has_changed('status_id'):
            body += f'\n- изменен статус c "{Status.objects.get(id=instance.tracker.previous("status_id"))}" на "{task.status}".'
        if instance.tracker.has_changed('user_id'):
            body += f'\n- изменен исполнитель c "{User.objects.get(id=instance.tracker.previous("user_id")).first_name} {User.objects.get(id=instance.tracker.previous("user_id")).last_name}" на "{task.user.first_name} {task.user.last_name}".'
        if instance.tracker.has_changed('deadline') and (instance.tracker.previous('deadline') != task.deadline):
            body += f'\n- изменен срок выполнения задачи на "{task.deadline}"'
        send_mail(subject, body, 'tussupbekov@gmail.com',
                  [instance.user.email, ], fail_silently=False)
