# Generated by Django 4.0.3 on 2022-03-15 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assignees',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
