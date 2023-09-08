from django.contrib import admin

from .models import *
# Register your models here.

class pageAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id', 'title')

class applAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','area')
    list_display_links = ('id','name','email')


class KursAdmin(admin.ModelAdmin):
    list_display = ('title', 'pricerub',)
    list_display_links = ('title',)


admin.site.register(Pages,pageAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Menu, MenuAdmin)

admin.site.register(Application, applAdmin)

admin.site.register(Kurs, KursAdmin)
