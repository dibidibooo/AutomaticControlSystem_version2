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


# Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
class ComponentsSite1(models.Model):
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    phosphorus = models.IntegerField(null=True, blank=True, verbose_name='Фосфор')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая')
    hardness_magnesium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость магниевая')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component1')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component1')


# Водоблок - 2 | Установка АВТ напротив погружного холодильника №42
class ComponentsSite2(models.Model):
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component2')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component2')


# Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-5,11.12
class ComponentsSite3(models.Model):
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    dry_residue = models.IntegerField(null=True, blank=True, verbose_name='Сухой остаток')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая')
    hardness_magnesium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость магниевая')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component3')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component3')


# БОВ-1 | Аналитическая точка насосов Р-02А/В/С
class ComponentsSite4(models.Model):
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component4')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component4')


# БОВ-1 | Аналитическая точка выкид насосов Р-01А/В/С/Д
class ComponentsSite5(models.Model):
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component5')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component5')


# БОВ-2 | Аналитическая точка насосов Р-01А/В/С/Д
class ComponentsSite6(models.Model):
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Общие Взвешенные вещества')
    alkalinity_phenols = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность по фенолу')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component6')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component6')


# УГОВ | Аналитическая точка насосов Р-01А/В/С/Д
class ComponentsSite7(models.Model):
    suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая (кальций, мг/л)')
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жесткость общая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component7')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component7')


# УГОВ | Выход из ёмкости 77-ТК-103 77-SN-004
class ComponentsSite8(models.Model):
    suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    phosphorus = models.IntegerField(null=True, blank=True, verbose_name='Фосфор')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая (кальций, мг/л)')
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component8')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component8')


# УГОВ | На входе в боковой фильтр позиции 77-Z-003 77-SN-006
class ComponentsSite9(models.Model):
    suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    phosphorus = models.IntegerField(null=True, blank=True, verbose_name='Фосфор')
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность')
    hardness_calcium = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость кальциевая (кальций, мг/л)')
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component9')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component9')


# УГОВ | Подача на градирню в районе 77-ТI-205 77-SN-007
class ComponentsSite10(models.Model):
    chlorine = models.IntegerField(null=True, blank=True, verbose_name='Остаточный хлор')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component10')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component10')


# УГОВ | На выходе с бокового фильтра 77-Z-003, 77-SN-008
class ComponentsSite11(models.Model):
    suspended_solids = models.IntegerField(null=True, blank=True, verbose_name='Общие взвешенные твердые частицы')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component11')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component11')


# МОС -> Очистные сооружения поз.119. С колодца промстоков №1 (точка №4 вход)
class ComponentsSite12(models.Model):
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
    ph = models.IntegerField(null=True, blank=True, verbose_name='pH')
    oxygen_chem = models.IntegerField(null=True, blank=True, verbose_name='Химическая потребность в кислороде (ХПК)')
    active_subst = models.IntegerField(null=True, blank=True, verbose_name='Поверхностно-активные вещества (АПАВ)')
    ammonium = models.IntegerField(null=True, blank=True, verbose_name='Аммонийный азот')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component12')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component12')


# БОС -> Пробоотборник 001 перед БОС / А1–SN-001
class ComponentsSite13(models.Model):
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
    ph = models.IntegerField(null=True, blank=True, verbose_name='Значение pH')
    oxygen_chem = models.IntegerField(null=True, blank=True, verbose_name='Химическая потребность в кислороде (ХПК)')
    active_subst = models.IntegerField(null=True, blank=True, verbose_name='Поверхностно-активные вещества (АПАВ)')
    ammonium = models.IntegerField(null=True, blank=True, verbose_name='Аммонийный азот')
    oxygen_bio = models.IntegerField(null=True, blank=True, verbose_name='Биологическая потребность в кислороде (БПК5)')
    phenols = models.IntegerField(null=True, blank=True, verbose_name='Фенолы')
    chlorides = models.IntegerField(null=True, blank=True, verbose_name='Хлориды')
    sulfates = models.IntegerField(null=True, blank=True, verbose_name='Сульфаты')
    iron = models.IntegerField(null=True, blank=True, verbose_name='Железо')
    nitrate = models.IntegerField(null=True, blank=True, verbose_name='Азот нитратов')
    nitrite = models.IntegerField(null=True, blank=True, verbose_name='Азот нитритов')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component13')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component13')


# БОС -> Сточная вода после биологических очистных сооружений А1–SN-009
class ComponentsSite14(models.Model):
    alkalinity = models.IntegerField(null=True, blank=True, verbose_name='Щёлочность общая')
    hardness = models.IntegerField(null=True, blank=True, verbose_name='Жёсткость общая')
    oxidability = models.IntegerField(null=True, blank=True, verbose_name='Окисляемость')
    salt = models.IntegerField(null=True, blank=True, verbose_name='Солесодержание')
    chlorine = models.IntegerField(null=True, blank=True, verbose_name='Остаточный хлор')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component14')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component14')


# БОС -> Выход с аппарата напорной флотации в ТК -008А/ А1 –SN -004А
class ComponentsSite15(models.Model):
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    oxygen_chem = models.IntegerField(null=True, blank=True, verbose_name='Химическая потребность в кислороде (ХПК)')
    ammonium = models.IntegerField(null=True, blank=True, verbose_name='Аммонийный азот')
    phosphorus = models.IntegerField(null=True, blank=True, verbose_name='Фосфор')
    oxygen_bio = models.IntegerField(null=True, blank=True, verbose_name='Биологическая потребность в кислороде (БПК5)')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component15')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component15')


# БОС -> Выход с аппарата напорной флотации в ТК-008В/ А1 –SN -004В
class ComponentsSite16(models.Model):
    suspended_subst = models.IntegerField(null=True, blank=True, verbose_name='Взвешенные вещества')
    oil_prod = models.IntegerField(null=True, blank=True, verbose_name='Нефтепродукт')
    oxygen_chem = models.IntegerField(null=True, blank=True, verbose_name='Химическая потребность в кислороде (ХПК)')
    ammonium = models.IntegerField(null=True, blank=True, verbose_name='Аммонийный азот')
    phosphorus = models.IntegerField(null=True, blank=True, verbose_name='Фосфор')
    oxygen_bio = models.IntegerField(null=True, blank=True, verbose_name='Биологическая потребность в кислороде (БПК5)')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время пробы')
    sampling_site = models.ForeignKey('projects.SamplingSite', on_delete=models.CASCADE, related_name='input_component16')
    water_type = models.ForeignKey('projects.WaterType', on_delete=models.CASCADE, related_name='input_component16')


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
