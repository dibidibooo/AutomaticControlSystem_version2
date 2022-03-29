# Generated by Django 4.0.3 on 2022-03-29 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_remove_component_limits_component_limit_hi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskassign',
            name='comp_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название компонента'),
        ),
        migrations.AddField(
            model_name='taskassign',
            name='sampling_site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_assign', to='projects.samplingsite'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание задачи'),
        ),
        migrations.AlterField(
            model_name='taskassign',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assign', to='projects.task'),
        ),
        migrations.AlterField(
            model_name='taskassign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_assign', to=settings.AUTH_USER_MODEL),
        ),
    ]