from django import forms

from projects.models import AdditionalComponents


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())
    smpl_site = forms.CharField(max_length=5, widget=forms.HiddenInput())


# Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
class Site1Form(MultipleForm):
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    suspended_solids = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные твердые частицы")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    phosphorus = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Фосфор")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость общая")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость кальциевая")
    hardness_magnesium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость магниевая")


# Водоблок - 2 | Установка АВТ напротив погружного холодильника №42
class Site2Form(MultipleForm):
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    suspended_solids = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные твердые частицы")


# Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-5,11.12
class Site3Form(MultipleForm):
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Взвешенные вещества")
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость общая")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо")
    dry_residue = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сухой остаток")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость кальциевая")
    hardness_magnesium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость магниевая")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")


# БОВ-1 | Аналитическая точка насосов Р-02А/В/С
class Site4Form(MultipleForm):
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость общая")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость кальциевая")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные вещества")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо")


# БОВ-1 | Аналитическая точка выкид насосов Р-01А/В/С/Д
class Site5Form(MultipleForm):
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость общая")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость кальциевая")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные вещества")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо")


# БОВ-2 | Аналитическая точка насосов Р-01А/В/С/Д
class Site6Form(MultipleForm):
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость общая")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость кальциевая")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные вещества")
    alkalinity_phenols = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность по фенолу")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо")


# УГОВ | Аналитическая точка насосов Р-01А/В/С/Д
class Site7Form(MultipleForm):
    suspended_solids = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные твердые частицы")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость кальциевая (кальций, мг/л)")
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость общая")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо общее")


# УГОВ | Выход из ёмкости 77-ТК-103 77-SN-004
class Site8Form(MultipleForm):
    suspended_solids = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные твердые частицы")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    phosphorus = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Фосфор")
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость кальциевая (кальций, мг/л)")
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость общая")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо общее")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")


# УГОВ | На входе в боковой фильтр позиции 77-Z-003 77-SN-006
class Site9Form(MultipleForm):
    suspended_solids = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные твердые частицы")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    phosphorus = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Фосфор")
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    hardness_calcium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жесткость кальциевая (кальций, мг/л)")
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость общая")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо общее")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")


# УГОВ | Подача на градирню в районе 77-ТI-205 77-SN-007
class Site10Form(MultipleForm):
    chlorine = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Остаточный хлор")
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")


# УГОВ | На выходе с бокового фильтра 77-Z-003, 77-SN-008
class Site11Form(MultipleForm):
    suspended_solids = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Общие взвешенные твердые частицы")


# МОС | Очистные сооружения поз.119. С колодца промстоков №1 (точка №4 вход)
class Site12Form(MultipleForm):
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Взвешенные вещества")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    oxygen_chem = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Химическая потребность в кислороде (ХПК)")
    active_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Поверхностно-активные вещества (АПАВ)")
    ammonium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Аммонийный азот")


# БОС | Пробоотборник 001 перед БОС / А1 –SN -001
class Site13Form(MultipleForm):
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Взвешенные вещества")
    ph = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3', 'max': 12, 'type': 'number'}), label="Значение pH")
    oxygen_chem = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Химическая потребность в кислороде (ХПК)")
    active_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Поверхностно-активные вещества (АПАВ)")
    ammonium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Аммонийный азот")
    oxygen_bio = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Биологическая потребность в кислороде (БПК5)")
    phenols = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Фенолы")
    chlorides = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Хлориды")
    sulfates = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Сульфаты")
    iron = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Железо")
    nitrate = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Азот нитратов")
    nitrite = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Азот нитритов")


# БОС | Сточная вода после биологических очистных сооружений А1 –SN -009
class Site14Form(MultipleForm):
    alkalinity = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Щёлочность общая")
    hardness = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Жёсткость общая")
    oxidability = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Окисляемость")
    salt = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Солесодержание")
    chlorine = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Остаточный хлор")


# БОС | Выход с аппарата напорной флотации в ТК -008А/ А1 –SN -004А
class Site15Form(MultipleForm):
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Взвешенные вещества")
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    oxygen_chem = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Химическая потребность в кислороде (ХПК)")
    ammonium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Аммонийный азот")
    phosphorus = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Фосфор")
    oxygen_bio = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Биологическая потребность в кислороде (БПК5)")


# БОС | Выход с аппарата напорной флотации в ТК-008В/ А1 –SN -004В
class Site16Form(MultipleForm):
    suspended_subst = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Взвешенные вещества")
    oil_prod = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Нефтепродукт")
    oxygen_chem = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Химическая потребность в кислороде (ХПК)")
    ammonium = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Аммонийный азот")
    phosphorus = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Фосфор")
    oxygen_bio = forms.FloatField(widget=forms.NumberInput(
        attrs={'class': 'form-control mb-3'}), label="Биологическая потребность в кислороде (БПК5)")


class AdditionalAnalysisForm(forms.ModelForm):
    class Meta:
        model = AdditionalComponents
        exclude = ['plant_unit']
        widgets = {
            'recycled_water_consumption': forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'True'}),
            'running_water_consumption': forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'True'}),
            'purge_flow': forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'True'}),
            'hot_water_temp': forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'True'}),
            'cold_water_temp': forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'True'}),
            'total_microbial_number': forms.NumberInput(attrs={'class': 'form-control mb-3', 'required': 'True'}),
        }
