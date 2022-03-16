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
    title = models.CharField(max_length=50, verbose_name='Название компонента')
    measurement = models.CharField(verbose_name='Единица измерения', max_length=50)
    limits = models.CharField(verbose_name='Допустимые нормы не более', max_length=50, blank=True)
    period = models.CharField(verbose_name='Периодичность отбора', max_length=100, blank=True)
    standards = models.CharField(verbose_name='Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField(verbose_name='Рекомендация выше нормы', max_length=200, null=True, blank=True)
    recommendation2 = models.CharField(verbose_name='Рекомендация ниже нормы', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Result(models.Model):
    component = models.ForeignKey('projects.Component', on_delete=models.CASCADE, related_name='result')
    value = models.IntegerField(null=True, blank=True, verbose_name='Показатель')


class Sample(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время анализа')
    sampling_site = models.ForeignKey('projects.SamplingSite', related_name='sample', on_delete=models.CASCADE)
    result = models.ForeignKey('projects.Result', related_name='sample', on_delete=models.CASCADE)


# class ComponentsSite1(models.Model):
#     oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
#     suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
#     ph = models.IntegerField(null=True, blank=True, verbose_name='pH')
#     oxygen_chem = models.IntegerField(null=True, blank=True, verbose_name='Химическая потребность в кислороде (ХПК)')
#     active_subst = models.IntegerField(null=True, blank=True, verbose_name='Поверхностно-активные вещества (АПАВ)')
#     ammonium = models.IntegerField(null=True, blank=True, verbose_name='Аммонийный азот')
#     datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
#     sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component1')
#     water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component1')
#     fk = models.ForeignKey('projects.Components1',
#                            on_delete=models.CASCADE,
#                            related_name='components_site1',
#                            blank=True,
#                            null=True)


# class ComponentsSite2(models.Model):
#     oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
#     suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
#     ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
#     oxygen_chem = models.IntegerField(null=True, blank=True, verbose_name='Химическая потребность в кислороде (ХПК)')
#     active_subst = models.IntegerField(null=True, blank=True, verbose_name='Поверхностно-активные вещества (АПАВ)')
#     ammonium = models.IntegerField(null=True, blank=True, verbose_name='Аммонийный азот')
#     oxygen_bio = models.IntegerField(null=True, blank=True, verbose_name='Биологическая потребность в кислороде (БПК5)')
#     phenols = models.IntegerField(null=True, blank=True, verbose_name='Фенолы')
#     chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
#     sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
#     iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
#     nitrate = models.IntegerField(null=True, blank=True, verbose_name='Азот нитратов')
#     nitrite = models.IntegerField(null=True, blank=True, verbose_name='Азот нитритов')
#     datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
#     sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component2')
#     water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component2')
#
#
# class ComponentsSite3(models.Model):
#     alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
#     hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
#     oxidability = models.IntegerField(null=True, blank=True, verbose_name='Окисляемость')
#     salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
#     chlorine = models.IntegerField(null=True, blank=True, verbose_name='Остаточный хлор')
#     datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
#     sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component3')
#     water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component3')
#
#
# class ComponentsSite4(models.Model):
#     oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
#     suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
#     ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
#     phosphorus = models.IntegerField(null=True, blank=True, verbose_name='Фосфор')
#     alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
#     hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
#     salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
#     chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
#     sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
#     iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
#     hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая')
#     hardness_magnesium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость магниевая')
#     datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
#     sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component4')
#     water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component4')
# ------------------------------------------
