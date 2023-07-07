from django.contrib import admin

from .models import *
# Register your models here.

class pageAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')



admin.site.register(Pages,pageAdmin)

admin.site.register(Category)
