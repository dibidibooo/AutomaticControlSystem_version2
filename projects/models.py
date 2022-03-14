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
        verbose_name = 'Словарь | Компоненты [1|1]'
        verbose_name_plural = 'Словарь | Компоненты [1|1]'


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
        verbose_name = 'Словарь | Компоненты [1|2]'
        verbose_name_plural = 'Словарь | Компоненты [1|2]'


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
        verbose_name = 'Словарь | Компоненты [1|3]'
        verbose_name_plural = 'Словарь | Компоненты [1|3]'


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
        verbose_name = 'Словарь | Компоненты [2|1]'
        verbose_name_plural = 'Словарь | Компоненты [2|1]'


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
        verbose_name = 'Словарь | Компоненты [2|2]'
        verbose_name_plural = 'Словарь | Компоненты [2|2]'


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
        verbose_name = 'Словарь | Компоненты [3|1]'
        verbose_name_plural = 'Словарь | Компоненты [3|1]'


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
        verbose_name = 'Словарь | Компоненты [4|1]'
        verbose_name_plural = 'Словарь | Компоненты [4|1]'


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
        verbose_name = 'Словарь | Компоненты [4|2]'
        verbose_name_plural = 'Словарь | Компоненты [4|2]'


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
        verbose_name = 'Словарь | Компоненты [4|3]'
        verbose_name_plural = 'Словарь | Компоненты [4|3]'


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
        verbose_name = 'Словарь | Компоненты [4|4]'
        verbose_name_plural = 'Словарь | Компоненты [4|4]'


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
        verbose_name = 'Словарь | Компоненты [4|5]'
        verbose_name_plural = 'Словарь | Компоненты [4|5]'


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
        verbose_name = 'Словарь | Компоненты [5|1]'
        verbose_name_plural = 'Словарь | Компоненты [5|1]'


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
        verbose_name = 'Словарь | Компоненты [6|1]'
        verbose_name_plural = 'Словарь | Компоненты [6|1]'


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
        verbose_name = 'Словарь | Компоненты [6|2]'
        verbose_name_plural = 'Словарь | Компоненты [6|2]'






# Оборотное водоснабжение Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
class InputComponent11(models.Model):
    input_component1 = models.IntegerField('Нефтепродукт')
    input_component2 = models.IntegerField('Значение рН')
    input_component3 = models.IntegerField('Общие взвешенные твердые частицы')
    input_component4 = models.IntegerField('Фосфор')
    input_component5 = models.IntegerField('Щелочность общая')
    input_component6 = models.IntegerField('Жесткость  общая')
    input_component7 = models.IntegerField('Солесодержание')
    input_component8 = models.IntegerField('Хлориды')
    input_component9 = models.IntegerField('Сульфаты')
    input_component10 = models.IntegerField('Жесткость кальциевая')
    input_component12 = models.IntegerField('Жесткость магниевая')
    input_component13 = models.IntegerField('Железо')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [1|1]'
        verbose_name_plural = 'Input | Компонент [1|1]'


# Оборотное водоснабжение Водоблок - 2 | Установка АВТ напротив погружного холодильника №42
class InputComponent12(models.Model):
    input_component1 = models.IntegerField('Нефтепродукт')
    input_component2 = models.IntegerField('Значение рН')
    input_component3 = models.IntegerField('Общие взвешенные твердые частицы')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [1|2]'
        verbose_name_plural = 'Input | Компонент [1|2]'


# Оборотное водоснабжение Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-5,11.12
class InputComponent13(models.Model):
    input_component1 = models.IntegerField('Взвешенные вещества')
    input_component2 = models.IntegerField('Жесткость общая')
    input_component3 = models.IntegerField('Железо')
    input_component4 = models.IntegerField('Сухой остаток')
    input_component5 = models.IntegerField('Щелочность общая')
    input_component6 = models.IntegerField('Солесодержание')
    input_component7 = models.IntegerField('Хлориды')
    input_component8 = models.IntegerField('Сульфаты')
    input_component9 = models.IntegerField('Жесткость кальциевая')
    input_component10 = models.IntegerField('Жесткость магниевая')
    input_component12 = models.IntegerField('Значение рН')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [1|3]'
        verbose_name_plural = 'Input | Компонент [1|3]'


# БОВ-1  | Аналитическая точка насосов Р-02А/В/С
class InputComponent21(models.Model):
    input_component1 = models.IntegerField('Общая жесткость')
    input_component2 = models.IntegerField('Кальциевая жесткость')
    input_component3 = models.IntegerField('Значение рН')
    input_component4 = models.IntegerField('Общее солесодержание')
    input_component5 = models.IntegerField('Содержание хлоридов')
    input_component6 = models.IntegerField('Содержание сульфатов')
    input_component7 = models.IntegerField('Содержание нефтепродуктов')
    input_component8 = models.IntegerField('Общие взвешенные вещества')
    input_component9 = models.IntegerField('Щелочность общая')
    input_component10 = models.IntegerField('Железо')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [2|1]'
        verbose_name_plural = 'Input | Компонент [2|1]'


# БОВ-1  | Аналитическая точка выкид насосов Р-01А/В/С/Д
class InputComponent22(models.Model):
    input_component1 = models.IntegerField('Общая жесткость')
    input_component2 = models.IntegerField('Кальциевая жесткость')
    input_component3 = models.IntegerField('Значение рН')
    input_component4 = models.IntegerField('Общее солесодержание')
    input_component5 = models.IntegerField('Содержание хлоридов')
    input_component6 = models.IntegerField('Содержание сульфатов')
    input_component7 = models.IntegerField('Содержание нефтепродуктов')
    input_component8 = models.IntegerField('Общие взвешенные вещества')
    input_component9 = models.IntegerField('Щелочность общая')
    input_component10 = models.IntegerField('Железо')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [2|2]'
        verbose_name_plural = 'Input | Компонент [2|2]'


# БОВ-1  | Аналитическая точка выкид насосов Р-01А/В/С/Д
class InputComponent31(models.Model):
    input_component1 = models.IntegerField('Общая жесткость')
    input_component2 = models.IntegerField('Кальциевая жесткость')
    input_component3 = models.IntegerField('Значение рН')
    input_component4 = models.IntegerField('Общее солесодержание')
    input_component5 = models.IntegerField('Содержание хлоридов')
    input_component6 = models.IntegerField('Содержание сульфатов')
    input_component7 = models.IntegerField('Содержание нефтепродуктов')
    input_component8 = models.IntegerField('Общие взвешенные вещества')
    input_component9 = models.IntegerField('Щелочность по фенолу')
    input_component10 = models.IntegerField('Щелочность общая')
    input_component11 = models.IntegerField('Железо')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [3|1]'
        verbose_name_plural = 'Input | Компонент [3|1]'


# УГОВ | Трубопровод подачи свежей воды из реки Урал (в районе клапанной сборки позиций 77-FV-203) 77-SN-001
class InputComponent41(models.Model):
    input_component1 = models.IntegerField('Общие взвешенные твердые частицы')
    input_component2 = models.IntegerField('Хлориды')
    input_component3 = models.IntegerField('Сульфаты')
    input_component4 = models.IntegerField('Значение рН')
    input_component5 = models.IntegerField('Щелочность общая')
    input_component6 = models.IntegerField('Жесткость кальциевая (кальций, мг/л)')
    input_component7 = models.IntegerField('Жесткость общая')
    input_component8 = models.IntegerField('Железо общее')
    input_component9 = models.IntegerField('Солесодержание')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [4|1]'
        verbose_name_plural = 'Input | Компонент [4|1]'


# УГОВ | Выход из ёмкости 77-ТК-103 77-SN-004
class InputComponent42(models.Model):
    input_component1 = models.IntegerField('Общие взвешенные твердые частицы')
    input_component2 = models.IntegerField('Значение рН')
    input_component3 = models.IntegerField('Хлориды')
    input_component4 = models.IntegerField('Фосфор')
    input_component5 = models.IntegerField('Нефтепродукт')
    input_component6 = models.IntegerField('Щелочность общая')
    input_component7 = models.IntegerField('Жесткость кальциевая (кальций, мг/л)')
    input_component8 = models.IntegerField('Жесткость общая')
    input_component9 = models.IntegerField('Железо общее')
    input_component10 = models.IntegerField('Солесодержание')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [4|2]'
        verbose_name_plural = 'Input | Компонент [4|2]'


# УГОВ | На входе в боковой фильтр позиции 77-Z-003 77-SN-006
class InputComponent43(models.Model):
    input_component1 = models.IntegerField('Общие взвешенные твердые частицы')
    input_component2 = models.IntegerField('Хлориды')
    input_component3 = models.IntegerField('Сульфаты')
    input_component4 = models.IntegerField('Значение рН')
    input_component5 = models.IntegerField('Фосфор')
    input_component6 = models.IntegerField('Щелочность')
    input_component7 = models.IntegerField('Жесткость кальциевая (кальций, мг/л)')
    input_component8 = models.IntegerField('Жесткость общая')
    input_component9 = models.IntegerField('Железо общее')
    input_component10 = models.IntegerField('Солесодержание')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [4|3]'
        verbose_name_plural = 'Input | Компонент [4|3]'



# УГОВ | Подача на градирню в районе 77-ТI-205 77-SN-007
class InputComponent44(models.Model):
    input_component1 = models.IntegerField('Остаточный хлор')
    input_component2 = models.IntegerField('Нефтепродукт')
    input_component3 = models.IntegerField('Солесодержание')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [4|4]'
        verbose_name_plural = 'Input | Компонент [4|4]'



# УГОВ | На выходе с бокового фильтра 77-Z-003, 77-SN-008
class InputComponent45(models.Model):
    input_component1 = models.IntegerField('Общие взвешенные твердые частицы')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [4|5]'
        verbose_name_plural = 'Input | Компонент [4|5]'


# МОС | Очистные сооружения поз.119. С колодца промстоков №1 (точка №4 вход)
class InputComponent51(models.Model):
    input_component1 = models.IntegerField('Нефтепродукт')
    input_component2 = models.IntegerField('Взвешенные вещества')
    input_component3 = models.IntegerField('Значение рН')
    input_component4 = models.IntegerField('Химическая потребность в кислороде (ХПК)')
    input_component5 = models.IntegerField('Поверхностно-активные вещества (АПАВ)')
    input_component6 = models.IntegerField('Аммонийный азот')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [5|1]'
        verbose_name_plural = 'Input | Компонент [5|1]'


# БОС | Пробоотборник 001 перед БОС / А1 –SN -001
class InputComponent61(models.Model):
    input_component1 = models.IntegerField('Значение рН')
    input_component2 = models.IntegerField('Взвешенные вещества')
    input_component3 = models.IntegerField('Химическая потребность в кислороде (ХПК)')
    input_component4 = models.IntegerField('Нефтепродукт')
    input_component5 = models.IntegerField('Биологическая потребность в кислороде (БПК5)')
    input_component6 = models.IntegerField('Фенолы')
    input_component7 = models.IntegerField('Поверхностно-активные вещества  (АПАВ)')
    input_component8 = models.IntegerField('Хлориды')
    input_component9 = models.IntegerField('Сульфаты')
    input_component10 = models.IntegerField('Железо')
    input_component11 = models.IntegerField('Аммонийный азот')
    input_component12 = models.IntegerField('Азот нитратов')
    input_component13 = models.IntegerField('Азот нитритов')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [6|1]'
        verbose_name_plural = 'Input | Компонент [6|1]'


# БОС | Сточная вода после биологических очистных сооружений А1 –SN -009
class InputComponent62(models.Model):
    input_component1 = models.IntegerField('Щёлочность общая')
    input_component2 = models.IntegerField('Жёсткость общая')
    input_component3 = models.IntegerField('Окисляемость')
    input_component4 = models.IntegerField('Солесодержание')
    input_component5 = models.IntegerField('Остаточный хлор')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Input | Компонент [6|2]'
        verbose_name_plural = 'Input | Компонент [6|2]'









# Оборотное водоснабжение Водоблок-2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
class Component11(models.Model):
    title_component = models.CharField('Название', max_length=50)
    title1 = models.CharField('Единица измерения', max_length=50)

    input_component1 = models.IntegerField('Щёлочность общая')

    title2 = models.CharField('Допустимые нормы не более', max_length=50, blank=True)
    title3 = models.CharField('Периодичность отбора', max_length=100, blank=True)
    title4 = models.CharField('Наименование НД и методы испытаний', max_length=100, blank=True)
    recommendation1 = models.CharField('Рекомендация выше нормы', max_length=100, blank=True)
    recommendation2 = models.CharField('Рекомендация ниже нормы', max_length=100, blank=True)
    key_component = models.ForeignKey(LocationPlace1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_component

    class Meta:
        verbose_name = 'Словарь | Компоненты [1|1]'
        verbose_name_plural = 'Словарь | Компоненты [1|1]'



