# Generated by Django 4.0.3 on 2022-03-10 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationplace1',
            options={'verbose_name': 'Отбор проб 1 | Водоблок', 'verbose_name_plural': 'Отбор проб 1 | Водоблок'},
        ),
        migrations.AlterModelOptions(
            name='locationplace2',
            options={'verbose_name': 'Отбор проб 2 | БОВ-1', 'verbose_name_plural': 'Отбор проб 2 | БОВ-1'},
        ),
        migrations.AlterModelOptions(
            name='locationplace3',
            options={'verbose_name': 'Отбор проб 3| БОВ-2', 'verbose_name_plural': 'Отбор проб 3 | БОВ-2'},
        ),
        migrations.AlterModelOptions(
            name='locationplace4',
            options={'verbose_name': 'Отбор проб 4| УГОВ', 'verbose_name_plural': 'Отбор проб 4 | УГОВ'},
        ),
        migrations.AlterModelOptions(
            name='locationplace5',
            options={'verbose_name': 'Отбор проб 5 | МОС', 'verbose_name_plural': 'Отбор проб 5 | МОС'},
        ),
        migrations.AlterModelOptions(
            name='locationplace6',
            options={'verbose_name': 'Отбор проб 6 | БОС', 'verbose_name_plural': 'Отбор проб 6 | БОС'},
        ),
        migrations.CreateModel(
            name='Component62',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace6')),
            ],
            options={
                'verbose_name': 'Компоненты [6|2] | Словарь',
                'verbose_name_plural': 'Компоненты [6|2] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component61',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace6')),
            ],
            options={
                'verbose_name': 'Компоненты [6|1] | Словарь',
                'verbose_name_plural': 'Компоненты [6|1] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component51',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace5')),
            ],
            options={
                'verbose_name': 'Компоненты [5|1] | Словарь',
                'verbose_name_plural': 'Компоненты [5|1] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component45',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace4')),
            ],
            options={
                'verbose_name': 'Компоненты [4|5] | Словарь',
                'verbose_name_plural': 'Компоненты [4|5] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component44',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace4')),
            ],
            options={
                'verbose_name': 'Компоненты [4|4] | Словарь',
                'verbose_name_plural': 'Компоненты [4|4] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component43',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace4')),
            ],
            options={
                'verbose_name': 'Компоненты [4|3] | Словарь',
                'verbose_name_plural': 'Компоненты [4|3] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component42',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace4')),
            ],
            options={
                'verbose_name': 'Компоненты [4|2] | Словарь',
                'verbose_name_plural': 'Компоненты [4|2] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component41',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace4')),
            ],
            options={
                'verbose_name': 'Компоненты [4|1] | Словарь',
                'verbose_name_plural': 'Компоненты [4|1] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component31',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace3')),
            ],
            options={
                'verbose_name': 'Компоненты [3|1] | Словарь',
                'verbose_name_plural': 'Компоненты [3|1] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace2')),
            ],
            options={
                'verbose_name': 'Компоненты [2|2] | Словарь',
                'verbose_name_plural': 'Компоненты [2|2] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component21',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace2')),
            ],
            options={
                'verbose_name': 'Компоненты [2|1] | Словарь',
                'verbose_name_plural': 'Компоненты [2|1] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace1')),
            ],
            options={
                'verbose_name': 'Компоненты [1|3] | Словарь',
                'verbose_name_plural': 'Компоненты [1|3] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace1')),
            ],
            options={
                'verbose_name': 'Компоненты [1|2] | Словарь',
                'verbose_name_plural': 'Компоненты [1|2] | Словарь',
            },
        ),
        migrations.CreateModel(
            name='Component11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_component', models.CharField(max_length=50, verbose_name='Название')),
                ('title1', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('title2', models.CharField(blank=True, max_length=50, verbose_name='Допустимые нормы не более')),
                ('title3', models.CharField(blank=True, max_length=100, verbose_name='Периодичность отбора')),
                ('title4', models.CharField(blank=True, max_length=100, verbose_name='Наименование НД и методы испытаний')),
                ('recommendation1', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=100, verbose_name='Рекомендация ниже нормы')),
                ('key_component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.locationplace1')),
            ],
            options={
                'verbose_name': 'Компоненты [1|1] | Словарь',
                'verbose_name_plural': 'Компоненты [1|1] | Словарь',
            },
        ),
    ]
