from django.contrib import admin
from django.contrib.gis import admin
from regions.models import Region
from leaflet.admin import LeafletGeoAdmin


class RegionAdmin(LeafletGeoAdmin):
    list_display = ('adm1alt1en', 'wkb_geometry')


admin.site.register(Region, RegionAdmin)
