from django.contrib import admin

from bell.models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(City,CityAdmin)





admin.site.register(Restra)
class DealAdmin(admin.ModelAdmin):
     list_display = ['id','restra_name']
admin.site.register(Deal,DealAdmin)

