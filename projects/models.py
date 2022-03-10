from django.db import models

# Водоблок -> [1|1] -> (оборотная вода)
# Водоблок -> [1|2] -> (оборотная вода)
# Водоблок -> [1|3] -> (оборотная вода)

# БОВ-1 -> [2|1] -> (подпиточная вода)
# БОВ-1 -> [2|2] -> (оборотная вода)

# БОВ-2 -> [3|1] -> (оборотная и подпиточная вода)

# УГОВ -> [4|1] -> (оборотная вода)
# УГОВ -> [4|2] -> (подпиточная вода)
# УГОВ -> [4|3] -> (оборотная вода)
# УГОВ -> [4|4] -> (оборотная вода)
# УГОВ -> [4|5] -> (оборотная вода)

# Create your models here.
class Location(models.Model):
    title_location = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title_location

    class Meta:
        verbose_name = 'Территория'
        verbose_name_plural = 'Территории'


class LocationPlace1(models.Model):
    title_locationplace = models.CharField('Название', max_length=100)
    places = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_locationplace

    class Meta:
        verbose_name = 'Отбор проб 1 | Водоблок'
        verbose_name_plural = 'Отбор проб 1 | Водоблок'

class LocationPlace2(models.Model):
    title_locationplace = models.CharField('Название', max_length=100)
    places = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_locationplace

    class Meta:
        verbose_name = 'Отбор проб 2 | БОВ-1'
        verbose_name_plural = 'Отбор проб 2 | БОВ-1'



class LocationPlace3(models.Model):
    title_locationplace = models.CharField('Название', max_length=100)
    places = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_locationplace

    class Meta:
        verbose_name = 'Отбор проб 3| БОВ-2'
        verbose_name_plural = 'Отбор проб 3 | БОВ-2'


class LocationPlace4(models.Model):
    title_locationplace = models.CharField('Название', max_length=100)
    places = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_locationplace

    class Meta:
        verbose_name = 'Отбор проб 4| УГОВ'
        verbose_name_plural = 'Отбор проб 4 | УГОВ'


class LocationPlace5(models.Model):
    title_locationplace = models.CharField('Название', max_length=100)
    places = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_locationplace

    class Meta:
        verbose_name = 'Отбор проб 5 | МОС'
        verbose_name_plural = 'Отбор проб 5 | МОС'


class LocationPlace6(models.Model):
    title_locationplace = models.CharField('Название', max_length=100)
    places = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_locationplace

    class Meta:
        verbose_name = 'Отбор проб 6 | БОС'
        verbose_name_plural = 'Отбор проб 6 | БОС'


class Water(models.Model):
    title_water = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title_water

    class Meta:
        verbose_name = 'Контролируемая вода'
        verbose_name_plural = 'Контролируемая вода'



# Оборотное водоснабжение Водоблок-2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
class Component11(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [1|1] | Словарь'
        verbose_name_plural = 'Компоненты [1|1] | Словарь'


# Оборотное водоснабжение Водоблок-2 | Установка АВТ напротив погружного холодильника №42
class Component12(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [1|2] | Словарь'
        verbose_name_plural = 'Компоненты [1|2] | Словарь'


# Оборотное водоснабжение Водоблок-2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-5,11.12
class Component13(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [1|3] | Словарь'
        verbose_name_plural = 'Компоненты [1|3] | Словарь'


# ПАУ БОВ-1 (титул 1026)/ПАУ БОВ-2 (титул 2602) | Аналитическая точка насосов Р-02А/В/С
class Component21(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace2, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [2|1] | Словарь'
        verbose_name_plural = 'Компоненты [2|1] | Словарь'


# ПАУ БОВ-1 (титул 1026)/ПАУ БОВ-2 (титул 2602) | Аналитическая точка выкид насосов Р-01А/В/С/Д
class Component22(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace2, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [2|2] | Словарь'
        verbose_name_plural = 'Компоненты [2|2] | Словарь'


# ПАУ БОВ-1 (титул 1026)/ПАУ БОВ-2 (титул 2602) | Аналитическая точка насосов Р-01А/В/С/Д
class Component31(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace3, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [3|1] | Словарь'
        verbose_name_plural = 'Компоненты [3|1] | Словарь'


# УГОВ ТОО «Enertek» | Трубопровод подачи свежей воды из реки Урал (в районе клапанной сборки позиций 77-FV-203) 77-SN-001
class Component41(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace4, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [4|1] | Словарь'
        verbose_name_plural = 'Компоненты [4|1] | Словарь'


# УГОВ ТОО «Enertek» | Выход из ёмкости 77-ТК-103 77-SN-004
class Component42(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace4, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [4|2] | Словарь'
        verbose_name_plural = 'Компоненты [4|2] | Словарь'


# УГОВ ТОО «Enertek» | На входе в боковой фильтр позиции 77-Z-003 77-SN-006
class Component43(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace4, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [4|3] | Словарь'
        verbose_name_plural = 'Компоненты [4|3] | Словарь'


# УГОВ ТОО «Enertek» | Подача на градирню в районе 77-ТI-205 77-SN-007
class Component44(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace4, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [4|4] | Словарь'
        verbose_name_plural = 'Компоненты [4|4] | Словарь'


# УГОВ ТОО «Enertek» | На выходе с бокового фильтра 77-Z-003, 77-SN-008
class Component45(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace4, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [4|5] | Словарь'
        verbose_name_plural = 'Компоненты [4|5] | Словарь'


# Механическая очистка | Очистные сооружения поз.119. С колодца промстоков №1 (точка №4 вход)
class Component51(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace5, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [5|1] | Словарь'
        verbose_name_plural = 'Компоненты [5|1] | Словарь'


# Биологическая очистка | Пробоотборник 001 перед БОС / А1 –SN -001
class Component61(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace6, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [6|1] | Словарь'
        verbose_name_plural = 'Компоненты [6|1] | Словарь'


# Биологическая очистка | Сточная вода после биологических очистных сооружений А1 –SN -009
class Component62(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)
    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace6, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Компоненты [6|2] | Словарь'
        verbose_name_plural = 'Компоненты [6|2] | Словарь'






# Оборотное водоснабжение Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
# class InputComponent11(models.Model):
#     input_component1 = models.IntegerField('Нефтепродукт')
#     input_component2 = models.IntegerField('Значение рН')
#     input_component3 = models.IntegerField('Общие взвешенные твердые частицы')
#     input_component4 = models.IntegerField('Фосфор')
#     input_component5 = models.IntegerField('Щелочность общая')
#     input_component6 = models.IntegerField('Щелочность общая')
#     input_component7 = models.IntegerField('Солесодержание')
#     input_component8 = models.IntegerField('Хлориды')
#     input_component9 = models.IntegerField('Сульфаты')
#     input_component10 = models.IntegerField('Жесткость кальциевая')
#     input_component12 = models.IntegerField('Жесткость магниевая')
#     input_component13 = models.IntegerField('Железо')
#     create_time = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Input | Показатель [1|1]'
#         verbose_name_plural = 'Input | Показатели [1|1]'


