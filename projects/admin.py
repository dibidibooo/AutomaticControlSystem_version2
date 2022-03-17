from django.contrib import admin
from .models import (
    PlantUnit,
    SamplingSite,
    WaterType,
Component,
ComponentsSite1,ComponentsSite2,ComponentsSite3,ComponentsSite4
)

admin.site.register(PlantUnit)
admin.site.register(SamplingSite)
admin.site.register(WaterType)

admin.site.register(Component)
admin.site.register(ComponentsSite1)
admin.site.register(ComponentsSite2)
admin.site.register(ComponentsSite3)
admin.site.register(ComponentsSite4)

