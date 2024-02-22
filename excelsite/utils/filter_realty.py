from korp.models import *
from crm.models import *

def go (request_get, filter_data, items):

    items_filtered=[]

    if 'square_from' in request_get:
        square_from = request_get.get('square_from')
        square_from = square_from.replace(' ', '')
        filter_data['square_from'] = square_from

    if 'square_to' in request_get:
        square_to = request_get.get('square_to')
        square_to = square_to.replace(' ', '')
        filter_data['square_to'] = square_to

    if 'filter_okrug' in request_get:
        filter_okrug = request_get.get('filter_okrug')
        filter_data['filter_okrug'] = filter_okrug


    for item in items:

        check = 1
        if ('filter_okrug' in locals()) and (filter_okrug != item.okrug ):
            check = 0

        if ('square_from' in locals()) and (len(square_from) > 0):
            try:
                if int(item.square) < int(square_from): check = 0
            except ValueError as ve:
                print('Цена должна быть числом')

        if ('square_to' in locals()) and (len(square_to) > 0):
            try:
                if int(item.square) > int(square_to): check = 0
            except ValueError as ve:
                print('Цена должна быть числом')

        if check == 1: items_filtered.append(item)

    return items_filtered