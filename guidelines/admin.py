"""
Admin for Guideline models
"""
from django.contrib import admin
import reversion

from guidelines import models

class GuidelineAdmin(reversion.VersionAdmin):
    filter_horizontal = 'diagnosis',
    search_fields = 'name',

admin.site.register(models.Guideline, GuidelineAdmin)