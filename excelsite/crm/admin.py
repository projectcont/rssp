from django.contrib import admin
from .models import *
from korp.models import Category

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'is_published', 'email', 'phone', )
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'phone','email',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    exclude = ['login','dop1', 'dop2','dop3','status',]

class ZayavkiAdmin(admin.ModelAdmin):
    list_display = ('id', 'categ','rentsale', 'square', 'price' , 'is_published', 'client', )
    list_display_links = ('id', 'categ',)
    list_editable = ('is_published',)
    list_filter = ('is_published','client','categ','rentsale',)

''' 
class ExportAdmin(admin.ModelAdmin):
    list_display = ( 'title','is_using',  )
'''

admin.site.register(Client, ClientAdmin)
admin.site.register(Zayavki, ZayavkiAdmin)

#admin.site.register(Export, ExportAdmin)
