from korp.models import *
#from utils.get_by_id import *
from utils.get_rentsale_ import get_rentsale

def context_items (menu_id):

    rentsale=get_rentsale(menu_id)

    print("menu_id=", menu_id, "rentsale=", rentsale)
    if rentsale=="rent":pricetype ="руб./месяц";
    if rentsale == "sale": pricetype = "руб.";
    doptitle = ""


    if menu_id==3:
        items = Ofis.objects.filter(is_published=True, rent=True).order_by('-time_create')
        metatitle='Офисы аренда, '
        metadescription = 'Офисы аренда'
        title =' Офисы (аренда)'

    if menu_id == 4:
        items = Torg.objects.filter(is_published=True, rent=True).order_by('-time_create')
        metatitle='Торговая площадь, аренда, '
        metadescription = 'Торговая площадь, аренда'
        title =' Торговая площадь (аренда)'

    if menu_id == 5 :
        items = Tc.objects.filter(is_published=True, rent=True).order_by('-time_create')
        metatitle='Здания, аренда, '
        metadescription = 'ТОРГОВЫЕ ЦЕНТРЫ, аренда'
        title ='Здания (аренда)'



    if menu_id == 7 :
        items = Proizv.objects.filter(is_published=True, rent=True).order_by('-time_create')
        metatitle='ПРОИЗВОДСТВО, аренда, '
        metadescription = 'ПРОИЗВОДСТВО, аренда'
        title =' ПРОИЗВОДСТВО (аренда)'

    if menu_id == 8:
        items = Sklad.objects.filter(is_published=True, rent=True).order_by('-time_create')
        metatitle='СКЛАДЫ, аренда, '
        metadescription = 'СКЛАДЫ, аренда'
        title ='СКЛАДЫ (аренда)'

    if menu_id == 9:
        items = Psn.objects.filter(is_published=True, rent=True).order_by('-time_create')
        metatitle='ПСН, аренда '
        metadescription = 'ПСН, аренда'
        title =' ПСН (аренда)'

    if menu_id == 10:
        items = Torg.objects.filter(is_published=True, rent=True, retail=True).order_by('-time_create')
        metatitle='РИТЕЙЛ, аренда '
        metadescription = 'РИТЕЙЛ, аренда'
        title ='РИТЕЙЛ (аренда)'

    if menu_id == 11:
        items = Land.objects.filter(is_published=True, rent=True).order_by('-time_create')
        metatitle='ЗЕМЛЯ, аренда '
        metadescription = 'ЗЕМЛЯ, аренда'
        title ='ЗЕМЛЯ (аренда)'

    #------------  sale   --------------------------------------------------------------

    if menu_id == 12 :
        items = Ofis.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' ОФИСЫ, продажа '
        metadescription = ' ОФИСЫ, продажа '
        title =' ОФИСЫ (продажа)'

    if menu_id == 13 :
        items = Torg.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' ТОРГОВАЯ ПЛОЩАДЬ, продажа '
        metadescription = ' ТОРГОВАЯ ПЛОЩАДЬ, продажа '
        title ='  ТОРГОВАЯ ПЛОЩАДЬ (продажа)'

    if menu_id == 14:
        items = Tc.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' Здания, продажа '
        metadescription = ' ТОРГОВЫЕ ЦЕНТРЫ, продажа '
        title ='  Здания (продажа)'


    if menu_id == 16:
        items = Proizv.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' ПРОИЗВОДСТВО, продажа '
        metadescription = ' ПРОИЗВОДСТВО, продажа '
        title ='  ПРОИЗВОДСТВО (продажа)'

    if menu_id == 17:
        items = Sklad.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' СКЛАДЫ, продажа '
        metadescription = ' СКЛАДЫ, продажа '
        title =' СКЛАДЫ (продажа)'

    if menu_id ==  18:
        items = Psn.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' ПСН, продажа '
        metadescription = ' ПСН, продажа '
        title ='  ПСН (продажа)'

    if menu_id == 19 :
        items = Torg.objects.filter(is_published=True, sale=True, retail=True).order_by('-time_create')
        metatitle=' РИТЕЙЛ, продажа '
        metadescription = ' РИТЕЙЛ, продажа '
        title ='  РИТЕЙЛ (продажа)'

    if menu_id == 20:
        items = Land.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' ЗЕМЛЯ, продажа '
        metadescription = ' ЗЕМЛЯ, продажа '
        title =' ЗЕМЛЯ (продажа)'

    if menu_id == 21:
        items = Flat.objects.filter(is_published=True, sale=True).order_by('-time_create')
        metatitle=' КВАРТИРЫ (НОВОСТРОЙКА), продажа '
        metadescription = ' КВАРТИРЫ (НОВОСТРОЙКА), продажа '
        title ='  КВАРТИРЫ НОВОСТРОЙКА (продажа)'


    context = {'title': title,'doptitle':doptitle, 'metatitle': metatitle, 'pricetype': pricetype, 'metadescription': metadescription,
                'items': items, 'menu_id':menu_id, 'rentsale':rentsale}

    return context




