from django.contrib import admin

from .import models


class OfficeAdmin(admin.ModelAdmin):
    list_display = ('named', 'location', 'picture')
    search_fields = ['named']
    list_filter = ['location']

admin.site.register(models.OfficesModel, OfficeAdmin)

# Register your models here.


class Members(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ['name']
    list_filter = ['position']


admin.site.register(models.MembersModel, Members)