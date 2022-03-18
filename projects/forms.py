from django import forms


class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())


# Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-14,15,16
class Site1Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Нефтепродукт")
    suspended_solids = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие взвешенные твердые частицы")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    phosphorus = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Фосфор")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость общая")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Солесодержание")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Хлориды")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Сульфаты")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость кальциевая")
    hardness_magnesium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость магниевая")



# Водоблок - 2 | Установка АВТ напротив погружного холодильника №42
class Site2Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Нефтепродукт")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    suspended_solids = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие взвешенные твердые частицы")



# Водоблок - 2 | Установка оборотного водоснабжения «Водоблок-2» с дренажей насосов Н-5,11.12
class Site3Form(MultipleForm):
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Взвешенные вещества")
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость общая")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо")
    dry_residue = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Сухой остаток")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Солесодержание")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Хлориды")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Сульфаты")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость кальциевая")
    hardness_magnesium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость магниевая")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")



# БОВ-1 | Аналитическая точка насосов Р-02А/В/С
class Site4Form(MultipleForm):
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общая жесткость")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Кальциевая жесткость")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общее солесодержание")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание хлоридов")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание сульфатов")
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание нефтепродуктов")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие Взвешенные вещества")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо")



# БОВ-1 | Аналитическая точка выкид насосов Р-01А/В/С/Д
class Site5Form(MultipleForm):
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общая жесткость")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Кальциевая жесткость")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общее солесодержание")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание хлоридов")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание сульфатов")
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание нефтепродуктов")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие Взвешенные вещества")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо")



# БОВ-2 | Аналитическая точка насосов Р-01А/В/С/Д
class Site6Form(MultipleForm):
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общая жесткость")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Кальциевая жесткость")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общее солесодержание")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание хлоридов")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание сульфатов")
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Содержание нефтепродуктов")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие Взвешенные вещества")
    alkalinity_fenol = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность по фенолу")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо")



# УГОВ | Аналитическая точка насосов Р-01А/В/С/Д
class Site7Form(MultipleForm):
    suspended_solids = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие взвешенные твердые частицы")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Хлориды")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Сульфаты")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Кальциевая жесткость (кальций, мг/л)")
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жесткость общая")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо общее")



# УГОВ | Выход из ёмкости 77-ТК-103 77-SN-004
class Site8Form(MultipleForm):
    suspended_solids = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие взвешенные твердые частицы")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Хлориды")
    phosphorus = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Фосфор")
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Нефтепродукт")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Кальциевая жесткость (кальций, мг/л)")
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость общая")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо общее")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Солесодержание")



# УГОВ | На входе в боковой фильтр позиции 77-Z-003 77-SN-006
class Site9Form(MultipleForm):
    suspended_solids = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие взвешенные твердые частицы")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Хлориды")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Сульфаты")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    phosphorus = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Фосфор")
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    hardness_calcium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Кальциевая жесткость (кальций, мг/л)")
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость общая")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо общее")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Солесодержание")



# УГОВ | Подача на градирню в районе 77-ТI-205 77-SN-007
class Site10Form(MultipleForm):
    chlorine = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Остаточный хлор")
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Нефтепродукт")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Солесодержание")



# УГОВ | На выходе с бокового фильтра 77-Z-003, 77-SN-008
class Site11Form(MultipleForm):
    suspended_solids = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Общие взвешенные твердые частицы")



# МОС | Очистные сооружения поз.119. С колодца промстоков №1 (точка №4 вход)
class Site12Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Нефтепродукт")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Взвешенные вещества")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="pH")
    oxygen_chem = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Химическая потребность в кислороде (ХПК)")
    active_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Поверхностно-активные вещества (АПАВ)")
    ammonium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Аммонийный азот")



# БОС | Пробоотборник 001 перед БОС / А1 –SN -001
class Site13Form(MultipleForm):
    oil_prod = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Нефтепродукт")
    suspended_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Взвешенные вещества")
    ph = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Значение pH")
    oxygen_chem = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Химическая потребность в кислороде (ХПК)")
    active_subst = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Поверхностно-активные вещества (АПАВ)")
    ammonium = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Аммонийный азот")
    oxygen_bio = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Биологическая потребность в кислороде (БПК5)")
    phenols = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Фенолы")
    chlorides = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Хлориды")
    sulfates = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Сульфаты")
    iron = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Железо")
    nitrate = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Азот нитратов")
    nitrite = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Азот нитритов")



# БОС | Сточная вода после биологических очистных сооружений А1 –SN -009
class Site14Form(MultipleForm):
    alkalinity = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Щёлочность общая")
    hardness = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Жёсткость общая")
    oxidability = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Окисляемость")
    salt = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Солесодержание")
    chlorine = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Остаточный хлор")










