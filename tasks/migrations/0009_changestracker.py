# Generated by Django 4.0.4 on 2022-04-19 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_task_responsible_alter_task_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangesTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000, verbose_name='Текст изменения')),
                ('updated_at', models.DateTimeField(verbose_name='Дата и время изменения')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='changes', to='tasks.task')),
            ],
        ),
    ]