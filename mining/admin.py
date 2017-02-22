from django.contrib import admin

from mining.models import *





class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Subject,SubjectAdmin)

admin.site.register(Chapter)
class ContentAdmin(admin.ModelAdmin):
     list_display = ['id','chapter_title']
admin.site.register(Content,ContentAdmin)

