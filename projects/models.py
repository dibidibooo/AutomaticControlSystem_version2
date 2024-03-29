from django.db import models


class PlantUnit(models.Model):
    title = models.CharField(verbose_name='Название установки', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Установка'
        verbose_name_plural = 'Установки'


class SamplingSite(models.Model):
    title = models.CharField(max_length=100, verbose_name='Место отбора проб')
    location = models.ForeignKey('projects.PlantUnit', on_delete=models.CASCADE, related_name='sampling_site')
    water_type = models.ManyToManyField('projects.WaterType', related_name='sampling_site')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место отбора проб'
        verbose_name_plural = 'Места отбора проб'


class WaterType(models.Model):
    type = models.CharField(max_length=50, verbose_name='Тип воды')

    def __str__(self):
        return self.type


class Component(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название компонента')
    measurement = models.CharField(verbose_name='Единица измерения', max_length=50)
    limit_lo = models.CharField(verbose_name='Допустимые нормы не ниже', max_length=50, null=True, blank=True)
    limit_hi = models.CharField(verbose_name='Допустимые нормы не более', max_length=50, null=True, blank=True)
    period = models.CharField(verbose_name='Периодичность отбора', max_length=100, blank=True)
    standards = models.CharField(verbose_name='Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField(verbose_name='Рекомендация выше нормы', max_length=200, null=True, blank=True)
    recommendation2 = models.CharField(verbose_name='Рекомендация ниже нормы', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class ComponentsSite(models.Model):
    active_subst = models.IntegerField(null=True, blank=True, verbose_name='Поверхностно-активные вещества (АПАВ)')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    alkalinity_phenols = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность по фенолу')
    ammonium = models.IntegerField(null=True, blank=True, verbose_name='Аммонийный азот')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    chlorine = models.IntegerField(null=True, blank=True, verbose_name='Остаточный хлор')
    dry_residue = models.IntegerField(null=True, blank=True, verbose_name='Сухой остаток')
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая')
    hardness_magnesium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость магниевая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    nitrate = models.IntegerField(null=True, blank=True, verbose_name='Азот нитратов')
    nitrite = models.IntegerField(null=True, blank=True, verbose_name='Азот нитритов')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    oxidability = models.IntegerField(null=True, blank=True, verbose_name='Окисляемость')
    oxygen_bio = models.IntegerField(null=True, blank=True, verbose_name='Биологическая потребность в кислороде (БПК5)')
    oxygen_chem = models.IntegerField(null=True, blank=True, verbose_name='Химическая потребность в кислороде (ХПК)')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    phenols = models.IntegerField(null=True, blank=True, verbose_name='Фенолы')
    phosphorus = models.IntegerField(null=True, blank=True, verbose_name='Фосфор')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')

    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    plant_unit = models.ForeignKey('projects.PlantUnit', on_delete=models.CASCADE, related_name='input_component')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component')


class Notification(models.Model):
    title = models.CharField(max_length=500, verbose_name='Уведомление')

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=25, verbose_name='Статус задачи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Statuses'


class AdditionalComponents(models.Model):
    plant_unit = models.ForeignKey('projects.PlantUnit', on_delete=models.CASCADE, related_name='additional_component')
    recycled_water_consumption = models.IntegerField(null=True, blank=True, verbose_name='Расход оборотной воды')
    running_water_consumption = models.IntegerField(null=True, blank=True, verbose_name='Расход подпиточной воды')
    purge_flow = models.IntegerField(null=True, blank=True, verbose_name='Расход продувки')
    hot_water_temp = models.IntegerField(null=True, blank=True, verbose_name='Температура горячей оборотной воды')
    cold_water_temp = models.IntegerField(null=True, blank=True, verbose_name='Температура охлажденной воды')
    total_microbial_number = models.IntegerField(null=True, blank=True, verbose_name='Общее микробное число')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')


class AdditionalCalculations(models.Model):
    evaporation_ratio = models.FloatField(null=True, blank=True, verbose_name='Коэффициент упаривания')
    calcium_hardness_transport = models.FloatField(null=True, blank=True, verbose_name='Транспорт кальциевой жесткости')
    purge_volume = models.FloatField(null=True, blank=True, verbose_name='Объем продувки')
    evaporative_loss = models.FloatField(null=True, blank=True, verbose_name='Потери с испарением')
    drip_loss = models.FloatField(null=True, blank=True, verbose_name='Капельный унос')
    unauthorized_loss = models.FloatField(null=True, blank=True, verbose_name='Несанкционированные потери')
    plant_unit = models.ForeignKey('projects.PlantUnit', on_delete=models.CASCADE, related_name='additional_calculation')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время расчета')
