from django.contrib import admin
from .models import Place,Question,Choice

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


class PlaceAdmin(ImportExportMixin,admin.ModelAdmin):
    pass

admin.site.register(Place)
admin.site.register(Question)
admin.site.register(Choice)

