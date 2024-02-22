from korp.models import *
from crm.models import *

def go ():
    """
    returns: количество всех объектов (с is_published=True)
    и количество всех заявок (с is_published=True)
    """
    all_items=[]

    ofis_items = Ofis.objects.filter(is_published=True)
    torg_items = Torg.objects.filter(is_published=True)
    tc_items =   Tc.objects.filter(is_published=True)
    proizv_items = Proizv.objects.filter(is_published=True)
    sklad_items = Sklad.objects.filter(is_published=True)
    psn_items = Psn.objects.filter(is_published=True)
    land_items = Land.objects.filter(is_published=True)
    flat_items = Flat.objects.filter(is_published=True)

    all_items.extend(ofis_items)
    all_items.extend(torg_items)
    all_items.extend(tc_items)
    all_items.extend(proizv_items)
    all_items.extend(sklad_items)
    all_items.extend(psn_items)

    all_items.extend(land_items)
    all_items.extend(flat_items)

    realty_bd_len = len(all_items)

    zavs = Zayavki.objects.filter(is_published=True)
    zavs_bd_len = len(zavs)

    return realty_bd_len, zavs_bd_len, all_items