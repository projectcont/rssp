from django.contrib import admin

from .forms import FormAdmin
from .models import *
from utils.fieldset import *



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
    form = FormAdmin
    list_display = ('id','worker', 'title',  'export_avito',  'is_published', 'adres', 'sale', 'rent')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published','export_avito',)
    list_filter = ('is_published',  'sale', 'rent', 'export_avito',)
    readonly_fields = ('categ','idl',)
    exclude = ['maplink','export_yandex','export_afi','export_domclik','export_5','export_6','metatitle','metadescription' ]
    fieldsets = (fieldset_osn, fieldset_sale, fieldset_rent, fieldset_export, fieldset_photos,)



class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price_sale', 'price_rent', 'is_published', 'adres', 'sale', 'rent')
    list_display_links = ('id', 'title')
    readonly_fields = ('categ', 'idl',)
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'sale', 'rent')
    exclude = ['maplink', 'export_yandex', 'export_afi', 'export_domclik', 'export_5', 'export_6', 'metatitle',
               'metadescription']
    fieldsets = (
        ('Основные свойства', {
            'fields': ('title', 'is_published', 'adres', 'map', 'square', 'photo', 'worker',
                       'owner', 'okrug', 'description',  'floor', 'floors', 'marketType', 'houseType', 'rooms', 'status', 'NewDevelopmentId','property_right', 'otdelka' )
        }),

        ('Продажа (при продаже заполнять обязательно)', {
            'fields': ('sale', 'price_sale', )
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


#-----

class LandAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'id', 'is_published', 'price_sale', 'price_rent', 'is_published', 'adres', 'sale', 'rent')
    list_display_links = ('id', 'title')
    readonly_fields = ('categ', 'idl',)
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'sale', 'rent')
    exclude = ['maplink', 'export_yandex', 'export_afi', 'export_domclik', 'export_5', 'export_6', 'metatitle',
               'metadescription']

    fieldset_osn= ('Основные свойства', {        'fields':    ('title', 'categ', 'idl', 'adres', 'map', 'landarea', 'photo', 'worker', 'owner', 'okrug', 'description', 'property_right', 'land_type')  })
    fieldset_sale = ('Продажа (при продаже заполнять обязательно)', { 'fields': ('sale', 'sale_type', 'price_sale', )
    })

    fieldset_rent = ('Аренда (при аренде заполнять обязательно)', {
        'fields': ('rent', 'rent_type', 'price_rent', 'lease', 'commission', )
    })


    fieldsets = (fieldset_osn, fieldset_sale, fieldset_rent, fieldset_export, fieldset_photos,)


class OfisAdmin(RealtyCommerceAdmin): pass

class ProizvAdmin(RealtyCommerceAdmin): pass
class SkladAdmin(RealtyCommerceAdmin): pass
class PsnAdmin(RealtyCommerceAdmin): pass

class TorgAdmin(RealtyCommerceAdmin):
    fieldset_osn=  ('Основные свойства',       {  'fields': ('title', 'is_published','categ', 'idl','retail','adres', 'map', 'square', 'photo', 'worker',     'owner', 'okrug', 'description', 'entrance', 'parking', 'buildtype', 'height', 'otdelka', 'floor', 'floors')      })
    fieldsets = (fieldset_osn, fieldset_sale, fieldset_rent, fieldset_export, fieldset_photos,)

class TcAdmin(RealtyCommerceAdmin):
    fieldset_osn = ('Основные свойства', {
        'fields': (  'title', 'is_published', 'categ', 'idl', 'adres', 'map', 'square', 'photo', 'worker', 'owner', 'okrug', 'description', 'parking', 'buildtype', 'otdelka', 'floors')
    })
    fieldsets = (fieldset_osn, fieldset_sale, fieldset_rent, fieldset_export, fieldset_photos,)


admin.site.register(Pages, PageAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Ofis, OfisAdmin)
admin.site.register(Torg, TorgAdmin)
admin.site.register(Proizv, ProizvAdmin)
admin.site.register(Sklad, SkladAdmin)
admin.site.register(Psn, PsnAdmin)
admin.site.register(Tc, TcAdmin)
admin.site.register(Flat, FlatAdmin)
admin.site.register(Land, LandAdmin)




