# Generated by Django 3.2.13 on 2022-05-07 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20220503_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentsSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_subst', models.IntegerField(blank=True, null=True, verbose_name='Поверхностно-активные вещества (АПАВ)')),
                ('alkalinity', models.IntegerField(blank=True, null=True, verbose_name='Щёлочность общая')),
                ('alkalinity_phenols', models.IntegerField(blank=True, null=True, verbose_name='Щёлочность по фенолу')),
                ('ammonium', models.IntegerField(blank=True, null=True, verbose_name='Аммонийный азот')),
                ('chlorides', models.IntegerField(blank=True, null=True, verbose_name='Хлориды')),
                ('chlorine', models.IntegerField(blank=True, null=True, verbose_name='Остаточный хлор')),
                ('dry_residue', models.IntegerField(blank=True, null=True, verbose_name='Сухой остаток')),
                ('hardness', models.IntegerField(blank=True, null=True, verbose_name='Жёсткость общая')),
                ('hardness_calcium', models.IntegerField(blank=True, null=True, verbose_name='Жёсткость кальциевая')),
                ('hardness_magnesium', models.IntegerField(blank=True, null=True, verbose_name='Жёсткость магниевая')),
                ('iron', models.IntegerField(blank=True, null=True, verbose_name='Железо')),
                ('nitrate', models.IntegerField(blank=True, null=True, verbose_name='Азот нитратов')),
                ('nitrite', models.IntegerField(blank=True, null=True, verbose_name='Азот нитритов')),
                ('oil_prod', models.IntegerField(blank=True, null=True, verbose_name='Нефтепродукт')),
                ('oxidability', models.IntegerField(blank=True, null=True, verbose_name='Окисляемость')),
                ('oxygen_bio', models.IntegerField(blank=True, null=True, verbose_name='Биологическая потребность в кислороде (БПК5)')),
                ('oxygen_chem', models.IntegerField(blank=True, null=True, verbose_name='Химическая потребность в кислороде (ХПК)')),
                ('ph', models.IntegerField(blank=True, null=True, verbose_name='Значение pH')),
                ('phenols', models.IntegerField(blank=True, null=True, verbose_name='Фенолы')),
                ('phosphorus', models.IntegerField(blank=True, null=True, verbose_name='Фосфор')),
                ('salt', models.IntegerField(blank=True, null=True, verbose_name='Солесодержание')),
                ('sulfates', models.IntegerField(blank=True, null=True, verbose_name='Сульфаты')),
                ('suspended_solids', models.IntegerField(blank=True, null=True, verbose_name='Общие взвешенные твердые частицы')),
                ('suspended_subst', models.IntegerField(blank=True, null=True, verbose_name='Взвешенные вещества')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')),
                ('plant_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_component', to='projects.plantunit')),
                ('sampling_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_component', to='projects.samplingsite')),
                ('water_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_component', to='projects.watertype')),
            ],
        ),
        migrations.RemoveField(
            model_name='componentssite10',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite10',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite11',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite11',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite12',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite12',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite13',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite13',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite14',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite14',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite15',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite15',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite16',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite16',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite2',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite2',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite3',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite3',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite4',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite4',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite5',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite5',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite6',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite6',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite7',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite7',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite8',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite8',
            name='water_type',
        ),
        migrations.RemoveField(
            model_name='componentssite9',
            name='sampling_site',
        ),
        migrations.RemoveField(
            model_name='componentssite9',
            name='water_type',
        ),
        migrations.DeleteModel(
            name='ComponentsSite1',
        ),
        migrations.DeleteModel(
            name='ComponentsSite10',
        ),
        migrations.DeleteModel(
            name='ComponentsSite11',
        ),
        migrations.DeleteModel(
            name='ComponentsSite12',
        ),
        migrations.DeleteModel(
            name='ComponentsSite13',
        ),
        migrations.DeleteModel(
            name='ComponentsSite14',
        ),
        migrations.DeleteModel(
            name='ComponentsSite15',
        ),
        migrations.DeleteModel(
            name='ComponentsSite16',
        ),
        migrations.DeleteModel(
            name='ComponentsSite2',
        ),
        migrations.DeleteModel(
            name='ComponentsSite3',
        ),
        migrations.DeleteModel(
            name='ComponentsSite4',
        ),
        migrations.DeleteModel(
            name='ComponentsSite5',
        ),
        migrations.DeleteModel(
            name='ComponentsSite6',
        ),
        migrations.DeleteModel(
            name='ComponentsSite7',
        ),
        migrations.DeleteModel(
            name='ComponentsSite8',
        ),
        migrations.DeleteModel(
            name='ComponentsSite9',
        ),
    ]