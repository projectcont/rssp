from korp.models import *
def go():
    all_items=[]

    ofis_items = Ofis.objects.filter()
    torg_items = Torg.objects.filter()
    tc_items = Tc.objects.filter()
    proizv_items = Proizv.objects.filter()
    sklad_items = Sklad.objects.filter()
    psn_items = Psn.objects.filter()
    retail_items = Retail.objects.filter()
    land_items = Land.objects.filter()
    flat_items = Flat.objects.filter()

    all_items.extend(ofis_items)
    all_items.extend(torg_items)
    all_items.extend(tc_items)
    all_items.extend(proizv_items)
    all_items.extend(sklad_items)
    all_items.extend(psn_items)
    all_items.extend(retail_items)
    all_items.extend(land_items)
    all_items.extend(flat_items)

    for item in all_items:
        if item.rent:
            if item.price_rent==None or item.rent_type==None:
                result_= f"<p> Объект {item.id} в части АРЕНДА не заполнены нужные поля </p> "
                print(result_)

        if item.sale:
            if item.price_sale == None or item.sale_type==None or item.sale_right==None:
                result_ = f"<p> Объект {item.id} {item.categ} в части ПРОДАЖА не заполнены нужные поля </p>"
                print(result_)

        if item.categ=='psn' or  item.categ=='food':
            if item.entrance == None:
                result_ = f"<p> Объект {item.id} {item.categ} ВХОД не указан </p>"
                print(result_)



    result=f" Всего {len(all_items)} объектов "
    result=result+result_
    return  result




