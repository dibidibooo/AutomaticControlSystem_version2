# Generated by Django 4.0.3 on 2022-03-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_inputcomponent11'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputComponent12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_component1', models.IntegerField(verbose_name='Нефтепродукт')),
                ('input_component2', models.IntegerField(verbose_name='Значение рН')),
                ('input_component3', models.IntegerField(verbose_name='Общие взвешенные твердые частицы')),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Input | Компонент [1|2]',
                'verbose_name_plural': 'Input | Компонент [1|2]',
            },
        ),
        migrations.CreateModel(
            name='InputComponent13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_component1', models.IntegerField(verbose_name='Взвешенные вещества')),
                ('input_component2', models.IntegerField(verbose_name='Жесткость общая')),
                ('input_component3', models.IntegerField(verbose_name='Железо')),
                ('input_component4', models.IntegerField(verbose_name='Сухой остаток')),
                ('input_component5', models.IntegerField(verbose_name='Щелочность общая')),
                ('input_component6', models.IntegerField(verbose_name='Солесодержание')),
                ('input_component7', models.IntegerField(verbose_name='Хлориды')),
                ('input_component8', models.IntegerField(verbose_name='Сульфаты')),
                ('input_component9', models.IntegerField(verbose_name='Жесткость кальциевая')),
                ('input_component10', models.IntegerField(verbose_name='Жесткость магниевая')),
                ('input_component12', models.IntegerField(verbose_name='Значение рН')),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Input | Компонент [1|3]',
                'verbose_name_plural': 'Input | Компонент [1|3]',
            },
        ),
        migrations.AlterModelOptions(
            name='component11',
            options={'verbose_name': 'Словарь | Компоненты [1|1]', 'verbose_name_plural': 'Словарь | Компоненты [1|1]'},
        ),
        migrations.AlterModelOptions(
            name='component12',
            options={'verbose_name': 'Словарь | Компоненты [1|2]', 'verbose_name_plural': 'Словарь | Компоненты [1|2]'},
        ),
        migrations.AlterModelOptions(
            name='component13',
            options={'verbose_name': 'Словарь | Компоненты [1|3]', 'verbose_name_plural': 'Словарь | Компоненты [1|3]'},
        ),
        migrations.AlterModelOptions(
            name='component21',
            options={'verbose_name': 'Словарь | Компоненты [2|1]', 'verbose_name_plural': 'Словарь | Компоненты [2|1]'},
        ),
        migrations.AlterModelOptions(
            name='component22',
            options={'verbose_name': 'Словарь | Компоненты [2|2]', 'verbose_name_plural': 'Словарь | Компоненты [2|2]'},
        ),
        migrations.AlterModelOptions(
            name='component31',
            options={'verbose_name': 'Словарь | Компоненты [3|1]', 'verbose_name_plural': 'Словарь | Компоненты [3|1]'},
        ),
        migrations.AlterModelOptions(
            name='component41',
            options={'verbose_name': 'Словарь | Компоненты [4|1]', 'verbose_name_plural': 'Словарь | Компоненты [4|1]'},
        ),
        migrations.AlterModelOptions(
            name='component42',
            options={'verbose_name': 'Словарь | Компоненты [4|2]', 'verbose_name_plural': 'Словарь | Компоненты [4|2]'},
        ),
        migrations.AlterModelOptions(
            name='component43',
            options={'verbose_name': 'Словарь | Компоненты [4|3]', 'verbose_name_plural': 'Словарь | Компоненты [4|3]'},
        ),
        migrations.AlterModelOptions(
            name='component44',
            options={'verbose_name': 'Словарь | Компоненты [4|4]', 'verbose_name_plural': 'Словарь | Компоненты [4|4]'},
        ),
        migrations.AlterModelOptions(
            name='component45',
            options={'verbose_name': 'Словарь | Компоненты [4|5]', 'verbose_name_plural': 'Словарь | Компоненты [4|5]'},
        ),
        migrations.AlterModelOptions(
            name='component51',
            options={'verbose_name': 'Словарь | Компоненты [5|1]', 'verbose_name_plural': 'Словарь | Компоненты [5|1]'},
        ),
        migrations.AlterModelOptions(
            name='component61',
            options={'verbose_name': 'Словарь | Компоненты [6|1]', 'verbose_name_plural': 'Словарь | Компоненты [6|1]'},
        ),
        migrations.AlterModelOptions(
            name='component62',
            options={'verbose_name': 'Словарь | Компоненты [6|2]', 'verbose_name_plural': 'Словарь | Компоненты [6|2]'},
        ),
        migrations.AlterModelOptions(
            name='inputcomponent11',
            options={'verbose_name': 'Input | Компонент [1|1]', 'verbose_name_plural': 'Input | Компонент [1|1]'},
        ),
        migrations.AlterField(
            model_name='inputcomponent11',
            name='input_component6',
            field=models.IntegerField(verbose_name='Жесткость  общая'),
        ),
    ]
