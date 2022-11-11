from django.contrib import admin

from .models import (
    PlantUnit,
    SamplingSite,
    WaterType,
    Component,
    ComponentFormula,
    AdditionalComponents,
    ComponentsSite,
    AdditionalCalculations
)


# class ComponentsSite(admin.)

admin.site.register(PlantUnit)
admin.site.register(SamplingSite)
admin.site.register(WaterType)
admin.site.register(Component)
admin.site.register(ComponentFormula)
admin.site.register(ComponentsSite)
admin.site.register(AdditionalComponents)
admin.site.register(AdditionalCalculations)
