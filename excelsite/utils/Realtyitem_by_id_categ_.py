from korp.models import *
def Realtyitem_by_id_categ (realty_id,realty_categ):
    if realty_categ == "ofis": item = Ofis.objects.get(pk=realty_id)
    if realty_categ == "torg": item = Torg.objects.get(pk=realty_id)
    if realty_categ == "tc": item = Tc.objects.get(pk=realty_id)
    if realty_categ == "proizv": item = Proizv.objects.get(pk=realty_id)
    if realty_categ == "slkad": item = Sklad.objects.get(pk=realty_id)
    if realty_categ == "psn": item = Psn.objects.get(pk=realty_id)
    if realty_categ == "retail": item = Retail.objects.get(pk=realty_id)
    if realty_categ == "land": item = Land.objects.get(pk=realty_id)
    if realty_categ == "flat": item = Flat.objects.get(pk=realty_id)
    return item
