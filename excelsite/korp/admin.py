from django.contrib import admin
from .models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', )

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'is_published', 'email', 'phone', )
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'phone','email',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    #exclude = ['login','dop1', 'dop2','dop3','status',]


class RealtyCommerceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price_sale', 'price_rent',  'is_published', 'adres', 'sale', 'rent')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published',  'sale', 'rent')
    readonly_fields = ('categ',)
    exclude = ['maplink','export_yandex','export_afi','export_domclik','export_5','export_6','metatitle','metadescription' ]
    fieldsets = (
        ('Основные свойства', {
            'fields': ('title', 'categ', 'adres', 'map', 'square', 'photo', 'worker',
                       'owner', 'okrug', 'description', 'entrance', 'parking', 'buildtype', 'height', 'otdelka','layout', 'floor', 'floors')
        }),

        ('Продажа (при продаже заполнять обязательно)', {
            'fields': ('sale', 'sale_type', 'price_sale', 'sale_right',)
        }),
        ('Аренда (при аренде заполнять обязательно)', {
            'fields': ('rent', 'rent_type','price_rent', )
        }),

        ('Экспорт', {
            'fields': (
            'export_avito', )
        }),


        ('Дополнительные фотографии (не обязательно)', {
            'fields': ('photo1','photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10', )
        }),
    )


class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price_sale', 'price_rent', 'is_published', 'adres', 'sale', 'rent')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'sale', 'rent')
    exclude = ['maplink', 'export_yandex', 'export_afi', 'export_domclik', 'export_5', 'export_6', 'metatitle',
               'metadescription']
    fieldsets = (
        ('Основные свойства', {
            'fields': ('title', 'adres', 'map', 'square', 'photo', 'worker',
                       'owner', 'okrug', 'description',  'floor', 'floors', 'marketType', 'houseType', 'rooms', 'status', 'NewDevelopmentId' )
        }),

        ('Продажа (при продаже заполнять обязательно)', {
            'fields': ('sale', 'sale_type', 'price_sale', 'sale_right',)
        }),
        ('Аренда (при аренде заполнять обязательно)', {
            'fields': ('rent', 'rent_type', 'price_rent',)
        }),

        ('Экспорт', {
            'fields': (
                'export_avito',)
        }),

        ('Дополнительные фотографии (не обязательно)', {
            'fields': (
            'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8', 'photo9', 'photo10',)
        }),
    )


class OfisAdmin(RealtyCommerceAdmin): pass
class TorgAdmin(RealtyCommerceAdmin): pass
class TcAdmin(RealtyCommerceAdmin): pass
class ProizvAdmin(RealtyCommerceAdmin): pass
class SkladAdmin(RealtyCommerceAdmin): pass
class PsnAdmin(RealtyCommerceAdmin): pass
class RetailAdmin(RealtyCommerceAdmin): pass
#class LandAdmin(RealtyCommerceAdmin): pass


admin.site.register(Pages, PageAdmin)
admin.site.register(Owner, OwnerAdmin)

admin.site.register(Ofis, OfisAdmin)
admin.site.register(Torg, TorgAdmin)
admin.site.register(Proizv, ProizvAdmin)
admin.site.register(Sklad, SkladAdmin)
admin.site.register(Psn, PsnAdmin)
admin.site.register(Retail, RetailAdmin)
admin.site.register(Tc, TcAdmin)
admin.site.register(Flat, FlatAdmin)
#admin.site.register(Land, LandAdmin)




