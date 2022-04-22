# Generated by Django 4.0.4 on 2022-04-22 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_samplingsite_water_type_and_more'),
        ('tasks', '0011_task_comp_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='water_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='projects.watertype'),
            preserve_default=False,
        ),
    ]
