# Generated by Django 4.0.3 on 2022-04-12 12:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskAssign',
            new_name='Task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='title',
        ),
    ]
