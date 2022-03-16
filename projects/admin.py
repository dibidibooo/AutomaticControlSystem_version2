from django.contrib import admin
from .models import (
    PlantUnit,
    SamplingSite,
    WaterType,
    Result,
    Sample
)

admin.site.register(PlantUnit)
admin.site.register(SamplingSite)
admin.site.register(WaterType)
admin.site.register(Result)
admin.site.register(Sample)
