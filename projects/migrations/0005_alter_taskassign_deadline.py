# Generated by Django 4.0.3 on 2022-03-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_tasks_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskassign',
            name='deadline',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Срок выполнения задачи'),
        ),
    ]
