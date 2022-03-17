from django.contrib import admin
from .models import (
    PlantUnit,
    SamplingSite,
    WaterType,
)

admin.site.register(PlantUnit)
admin.site.register(SamplingSite)
admin.site.register(WaterType)
