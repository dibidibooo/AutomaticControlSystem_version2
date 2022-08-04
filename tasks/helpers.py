from datetime import timedelta, datetime

from django.conf import settings
from django.template import loader

from accounts.models import Profile
from projects.helpers import send_html_mail
from tasks.models import Task


def archive_task():
    for task in Task.objects.all():
        if task.completion_date and task.status_id == 4:
            date_to_archive = task.completion_date + timedelta(days=3)
            if date_to_archive <= datetime.now():
                task.status_id = 5
                task.save()


def send_email_to_director():
    # Отправка email уведомлений Директору, если задача не была назначена 2 или более дней
    for task in Task.objects.all():
        no_changes_in_2_days = task.start_date + timedelta(days=2)
        if task.status_id == 1 and no_changes_in_2_days <= datetime.now() and task.notified is False:
            from_email = settings.EMAIL_HOST_USER
            val = {
                'task_id': task.pk,
                'task_title': task.title,
                'component': task.comp_title,
                'sampling_site': task.sampling_site,
                'plant_unit': task.plant_unit,
            }
            html_message = loader.render_to_string('emails/task_not_assigned.html', val)

            director_email = Profile.objects.get(position='Нач установки').user.email
            to_email = [director_email]

            subject = f'Задача не назначена'

            send_html_mail(subject=subject, html_content=html_message, recipient_list=to_email, sender=from_email)
            task.notified = True
            task.save()
