from korp.models import *
from proc.get_by_id import *
from proc.get_rentsale_ import get_rentsale

def context_items (menu_id):

    rentsale=get_rentsale(menu_id)

    print("menu_id=", menu_id, "rentsale=", rentsale)
    if rentsale=="rent":pricetype ="руб./месяц";
    if rentsale == "sale": pricetype = "руб.";
    doptitle = ""


    if menu_id==3:
        items = Ofis.objects.filter(is_published=True, rent=True)
        metatitle='Офисы аренда, '
        metadescription = 'Офисы аренда'
        title =' Офисы (аренда)'

    if menu_id == 4:
        items = Torg.objects.filter(is_published=True, rent=True)
        metatitle='Торговая площадь, аренда, '
        metadescription = 'Торговая площадь, аренда'
        title =' Торговая площадь (аренда)'

    if menu_id == 5 :
        items = Tc.objects.filter(is_published=True, rent=True)
        metatitle='Здания, аренда, '
        metadescription = 'ТОРГОВЫЕ ЦЕНТРЫ, аренда'
        title ='Здания (аренда)'



    if menu_id == 7 :
        items = Proizv.objects.filter(is_published=True, rent=True)
        metatitle='ПРОИЗВОДСТВО, аренда, '
        metadescription = 'ПРОИЗВОДСТВО, аренда'
        title =' ПРОИЗВОДСТВО (аренда)'

    if menu_id == 8:
        items = Sklad.objects.filter(is_published=True, rent=True)
        metatitle='СКЛАДЫ, аренда, '
        metadescription = 'СКЛАДЫ, аренда'
        title ='СКЛАДЫ (аренда)'

    if menu_id == 9:
        items = Psn.objects.filter(is_published=True, rent=True)
        metatitle='ПСН, аренда '
        metadescription = 'ПСН, аренда'
        title =' ПСН (аренда)'

    if menu_id == 10:
        items = Retail.objects.filter(is_published=True, rent=True)
        metatitle='РИТЕЙЛ, аренда '
        metadescription = 'РИТЕЙЛ, аренда'
        title ='РИТЕЙЛ (аренда)'

    if menu_id == 11:
        items = Land.objects.filter(is_published=True, rent=True)
        metatitle='ЗЕМЛЯ, аренда '
        metadescription = 'ЗЕМЛЯ, аренда'
        title ='ЗЕМЛЯ (аренда)'

    #------------  sale   --------------------------------------------------------------

    if menu_id == 12 :
        items = Ofis.objects.filter(is_published=True, sale=True)
        metatitle=' ОФИСЫ, продажа '
        metadescription = ' ОФИСЫ, продажа '
        title =' ОФИСЫ (продажа)'

    if menu_id == 13 :
        items = Torg.objects.filter(is_published=True, sale=True)
        metatitle=' ТОРГОВАЯ ПЛОЩАДЬ, продажа '
        metadescription = ' ТОРГОВАЯ ПЛОЩАДЬ, продажа '
        title ='  ТОРГОВАЯ ПЛОЩАДЬ (продажа)'

    if menu_id == 14:
        items = Tc.objects.filter(is_published=True, sale=True)
        metatitle=' Здания, продажа '
        metadescription = ' ТОРГОВЫЕ ЦЕНТРЫ, продажа '
        title ='  Здания (продажа)'


    if menu_id == 16:
        items = Proizv.objects.filter(is_published=True, sale=True)
        metatitle=' ПРОИЗВОДСТВО, продажа '
        metadescription = ' ПРОИЗВОДСТВО, продажа '
        title ='  ПРОИЗВОДСТВО (продажа)'

    if menu_id == 17:
        items = Sklad.objects.filter(is_published=True, sale=True)
        metatitle=' СКЛАДЫ, продажа '
        metadescription = ' СКЛАДЫ, продажа '
        title =' СКЛАДЫ (продажа)'

    if menu_id ==  18:
        items = Psn.objects.filter(is_published=True, sale=True)
        metatitle=' ПСН, продажа '
        metadescription = ' ПСН, продажа '
        title ='  ПСН (продажа)'

    if menu_id == 19 :
        items = Retail.objects.filter(is_published=True, sale=True)
        metatitle=' РИТЕЙЛ, продажа '
        metadescription = ' РИТЕЙЛ, продажа '
        title ='  РИТЕЙЛ (продажа)'

    if menu_id == 20:
        items = Land.objects.filter(is_published=True, sale=True)
        metatitle=' ЗЕМЛЯ, продажа '
        metadescription = ' ЗЕМЛЯ, продажа '
        title =' ЗЕМЛЯ (продажа)'

    if menu_id == 21:
        items = Flat.objects.filter(is_published=True, sale=True)
        metatitle=' КВАРТИРЫ (НОВОСТРОЙКА), продажа '
        metadescription = ' КВАРТИРЫ (НОВОСТРОЙКА), продажа '
        title ='  КВАРТИРЫ НОВОСТРОЙКА (продажа)'


    context = {'title': title,'doptitle':doptitle, 'metatitle': metatitle, 'pricetype': pricetype, 'metadescription': metadescription,
                'items': items, 'menu_id':menu_id, 'rentsale':rentsale}

    return context




