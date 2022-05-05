from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models import signals
from django.template import loader

from projects.helpers import send_html_mail
from projects.models import Status
from django.conf import settings
from .models import Task


@receiver(signals.post_save, sender=Task)
def task_send_email(sender, instance, created, **kwargs):
    task = Task.objects.get(id=instance.id)

    if instance.user and instance.user.email and (
            instance.tracker.has_changed('status_id') or
            instance.tracker.has_changed('user_id') or (instance.tracker.previous('deadline') != task.deadline)):
        val = {
            'task': instance,
            'prev_status': Status.objects.get(id=instance.tracker.previous("status_id")),
        }
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.user.email, ]
        subject = f'Изменения в задаче #{instance.id}'
        body = f"""В задаче №{instance.id} - {instance.title} для компонента {instance.comp_title}
(Место отбора проб: {instance.sampling_site}. Установка: {instance.plant_unit}.):"""

        if instance.tracker.has_changed('status_id'):
            body += f'\n- изменен статус c "{Status.objects.get(id=instance.tracker.previous("status_id"))}" на "{task.status}".'
        if instance.tracker.has_changed('user_id'):
            if instance.tracker.previous("user_id") is None:
                body += f'\n- изменен исполнитель на "{task.user.first_name} {task.user.last_name}".'
            else:
                val['prev_assignee'] = User.objects.get(id=instance.tracker.previous("user_id"))
                body += f'\n- изменен исполнитель c "{User.objects.get(id=instance.tracker.previous("user_id")).first_name} {User.objects.get(id=instance.tracker.previous("user_id")).last_name}" на "{task.user.first_name} {task.user.last_name}".'
        if instance.tracker.has_changed('deadline') and (instance.tracker.previous('deadline') != task.deadline):
            task_deadline = task.deadline.strftime("%d.%m.%Y %H:%M")
            val['deadline'] = task_deadline
            body += f'\n- изменен срок выполнения задачи на "{task_deadline}"'

        html_message = loader.render_to_string('emails/task_update.html', val)
        body += '\n\nПройдите по ссылке, чтобы открыть доску задач: http://127.0.0.1:8000/tasks/kanbanboard'

        send_html_mail(subject=subject, html_content=html_message, recipient_list=to_email, sender=from_email)
