from django.contrib import admin

from .models import (
    PlantUnit,
    SamplingSite,
    WaterType,
    Component,
    AdditionalComponents,
    ComponentsSite
)

admin.site.register(PlantUnit)
admin.site.register(SamplingSite)
admin.site.register(WaterType)
admin.site.register(Component)
admin.site.register(ComponentsSite)
admin.site.register(AdditionalComponents)
