# Generated by Django 4.0.3 on 2022-03-24 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='componentssite6',
            old_name='alkalinity_fenol',
            new_name='alkalinity_phenols',
        ),
    ]