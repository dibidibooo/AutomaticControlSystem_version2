from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models import signals

from .models import Task


@receiver(signals.post_save, sender=Task)
def send_task_send_email(sender, instance, created, **kwargs):
    if not instance.user:
        print(f'{instance} has no assignee')
    elif instance.user and instance.user.email:
        body = f"""
        Произведены изменения в задаче '{instance.title}' для компонента '{instance.comp_title}'.
        Изменен исполнитель в задаче на {instance.user.first_name} {instance.user.last_name}.
        Место отбора проб {instance.sampling_site}.
        Установка {instance.plant_unit}.
        """
        subject = f"Изменения в задаче #{instance.id}"
        send_mail(subject, body, 'tussupbekov@gmail.com',
                  [instance.user.email, ], fail_silently=False,)
