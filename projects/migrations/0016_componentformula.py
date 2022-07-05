# Generated by Django 3.2.13 on 2022-07-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_componentssite_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentFormula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название компонента')),
                ('limit_lo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Допустимые нормы не ниже')),
                ('limit_hi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Допустимые нормы не более')),
                ('recommendation1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Рекомендация выше нормы')),
                ('recommendation2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Рекомендация ниже нормы')),
            ],
        ),
    ]