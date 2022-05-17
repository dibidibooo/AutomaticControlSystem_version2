from datetime import timedelta, datetime
from celery import shared_task
from tasks.models import Task


@shared_task(name='archive_task')
def archive_task():
    for task in Task.objects.all():
        if task.completion_date and task.status_id == 4:
            date_to_archive = task.completion_date + timedelta(days=3)
            if date_to_archive <= datetime.now():
                task.status_id = 5
                task.save()
