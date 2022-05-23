# Generated by Django 3.2.13 on 2022-05-19 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tasks', '0014_changestracker_failure_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_responsible', to='auth.group', verbose_name='Ответственный'),
        ),
    ]