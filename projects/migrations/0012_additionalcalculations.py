# Generated by Django 3.2.13 on 2022-05-11 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20220507_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalCalculations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaporation_ratio', models.IntegerField(blank=True, null=True, verbose_name='Коэффициент упаривания')),
                ('calcium_hardness_transport', models.IntegerField(blank=True, null=True, verbose_name='Транспорт кальциевой жесткости')),
                ('purge_volume', models.IntegerField(blank=True, null=True, verbose_name='Объем продувки')),
                ('evaporative_loss', models.IntegerField(blank=True, null=True, verbose_name='Потери с испарением')),
                ('drip_loss', models.IntegerField(blank=True, null=True, verbose_name='Капельный унос')),
                ('unauthorized_loss', models.IntegerField(blank=True, null=True, verbose_name='Несанкционированные потери')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время расчета')),
                ('plant_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_calculation', to='projects.plantunit')),
            ],
        ),
    ]
