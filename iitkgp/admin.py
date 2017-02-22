from django.contrib import admin

from iitkgp.models import *



class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Department,DepartmentAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Subject,SubjectAdmin)

admin.site.register(Chapter)
class ContentAdmin(admin.ModelAdmin):
     list_display = ['id','chapter_title']
admin.site.register(Content,ContentAdmin)

