# Generated by Django 4.0.4 on 2022-04-19 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_delete_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='period_in_hours',
        ),
    ]