# Generated by Django 3.2.13 on 2022-08-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_task_responsible'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
