from korp.models import *
from crm.models import *

def go ():
    zavs = Zayavki.objects.all()


    zavs_filtered=[]




    for zav in zavs:

        check = 1
        if ('filter_categ' in locals()) and (filter_categ != "notchosen"):
            #print('filter_categ',filter_categ, zav.categ)
            if zav.categ != filter_categ: check = 0

        if ('filter_rentsale' in locals()) and (filter_rentsale != "notchosen"):
            #print('filter_rentsale',filter_rentsale, zav.rentsale)
            if zav.rentsale != filter_rentsale: check = 0

        if ('price_from' in locals()) and (len(price_from) > 0):
            try:
                if int(zav.price) < int(price_from): check = 0
            except ValueError as ve:
                print('Цена должна быть числом')

        if ('price_to' in locals()) and (len(price_to) > 0):
            try:
                if int(zav.price) > int(price_to): check = 0
            except ValueError as ve:
                print('Цена должна быть числом')

        if check == 1: zavs_filtered.append(zav)

    return zavs_filtered