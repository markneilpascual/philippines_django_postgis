from django.db import models
from django.contrib.gis.db import models as geomodels


class Region(models.Model):
    adm1alt1en = models.CharField(max_length=100, blank=False)
    wkb_geometry = geomodels.MultiPolygonField()

    class Meta:
        verbose_name_plural = 'regions'
        # order of drop-down list items
        ordering = ('adm1alt1en',)

