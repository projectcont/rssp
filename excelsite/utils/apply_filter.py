from korp.models import *
from crm.models import *

def go (request_get, filter_data, zavs):

    zavs_filtered=[]


    if 'filter_categ' in request_get:
        filter_categ = request_get.get('filter_categ');
        filter_data['filter_categ'] = filter_categ

    if 'filter_rentsale' in request_get:
        filter_rentsale = request_get.get('filter_rentsale')
        filter_data['filter_rentsale'] = filter_rentsale

    if 'price_from' in request_get:
        price_from = request_get.get('price_from')
        price_from = price_from.replace(' ', '')
        filter_data['price_from'] = price_from

    if 'price_to' in request_get:
        price_to = request_get.get('price_to')
        price_to = price_to.replace(' ', '')
        filter_data['price_to'] = price_to

    if 'price_from' in request_get:
        price_from = request_get.get('price_from')
        price_from = price_from.replace(' ', '')
        filter_data['price_from'] = price_from

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