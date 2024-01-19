from korp.models import *

def go(price, square, okrug_list, categ, rentsale):

    #--- выбираются объекты только из нужной категории (которая соотв категоиии в заявке)

    if (categ == 'ofis' and rentsale == 'rent'): realty_items = Ofis.objects.filter(is_published=True, rent=True)
    if (categ == 'ofis' and rentsale == 'sale'): realty_items = Ofis.objects.filter(is_published=True, sale=True)

    if (categ == 'torg' and rentsale == 'rent'): realty_items = Torg.objects.filter(is_published=True, rent=True)
    if (categ == 'torg' and rentsale == 'sale'): realty_items = Torg.objects.filter(is_published=True, sale=True)

    if (categ == 'tc' and rentsale == 'rent'): realty_items = Tc.objects.filter(is_published=True, rent=True)
    if (categ == 'tc' and rentsale == 'sale'): realty_items = Tc.objects.filter(is_published=True, sale=True)


    if (categ == 'proizv' and rentsale == 'rent'): realty_items = Proizv.objects.filter(is_published=True, rent=True)
    if (categ == 'proizv' and rentsale == 'sale'): realty_items = Proizv.objects.filter(is_published=True, sale=True)

    if (categ == 'sklad' and rentsale == 'rent'): realty_items = Sklad.objects.filter(is_published=True, rent=True)
    if (categ == 'sklad' and rentsale == 'sale'): realty_items = Sklad.objects.filter(is_published=True, sale=True)

    if (categ == 'psn' and rentsale == 'rent'): realty_items = Psn.objects.filter(is_published=True, rent=True)
    if (categ == 'psn' and rentsale == 'sale'): realty_items = Psn.objects.filter(is_published=True, sale=True)

    if (categ == 'retail' and rentsale == 'rent'): realty_items = Retail.objects.filter(is_published=True, rent=True)
    if (categ == 'retail' and rentsale == 'sale'): realty_items = Retail.objects.filter(is_published=True, sale=True)

    if (categ == 'land' and rentsale == 'rent'): realty_items = Land.objects.filter(is_published=True, rent=True)
    if (categ == 'land' and rentsale == 'sale'): realty_items = Land.objects.filter(is_published=True, sale=True)

    if (categ == 'flat' and rentsale == 'rent'): realty_items = Flat.objects.filter(is_published=True, rent=True)
    if (categ == 'flat' and rentsale == 'sale'): realty_items = Flat.objects.filter(is_published=True, sale=True)


    # --- лист подходящих объектов
    realty_items_selected=[]

    for n in realty_items:

        if rentsale=='rent': n_price = n.price_rent
        else: n_price =n.price_sale

        if (n_price<=price) and (n.square>=square) :
            print('okrug=',n.okrug, okrug_list)

            if '1000' in okrug_list:
                realty_items_selected.append(n)
            else:
                if n.okrug in okrug_list:
                    realty_items_selected.append(n)

    return realty_items_selected






