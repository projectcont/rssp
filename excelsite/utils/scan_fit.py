from korp.models import *
from crm.models import *

def fit (item, zav, price_offset:float, square_offset:float, fits_number:int ):

    """
    метод проверяет, данный объект (item) подходит ли для данной заявки (zav)
    если подходит, вписывает в базу  zav.scan с дополнением id-объекта
     если подходит, вписывает в базу  item.scan с дополнением id-заявки
    """

    check = 1
    if zav.categ != item.categ: check = 0
    if (zav.rentsale == "rent") and (item.rent == False):  check = 0
    if (zav.rentsale == "sale") and (item.sale == False): check = 0

    if (zav.rentsale == "sale") and (item.price_sale is not None):
        if (item.price_sale > (zav.price + price_offset)) or (item.price_sale < (zav.price - price_offset)): check = 0

    if (zav.rentsale == "rent") and (item.price_rent is not None):
        if (item.price_rent > (zav.price + price_offset)) or (item.price_rent < (zav.price - price_offset)): check = 0

    if (item.square > (zav.square + square_offset)) or (item.square < (zav.square - square_offset)): check = 0


    zavokrug_list=list(zav.okrug)

    # заявка - вне Москвы,  объект в Москве, или наоборот
    if ((zav.okrug=="1001") and (item.okrug!="13")) or  ((zav.okrug!="1001") and (item.okrug=="13")): check = 0
    #   объект с округом, который входит в округи заявки

    if ("1000" not in zavokrug_list ):
        if item.okrug not in zavokrug_list: check = 0


    ''' 
    if item.pk==6 and zav.pk==30:
        print("????item.pk",item.pk,"zav.pk",zav.pk, "check=", check,"item.okrug=", item.okrug,"zavokrug_list=", zavokrug_list,  )
        print("----------------------------------------------" )
        input()
    '''


    if check == 1:
        # добавление в завяку подходящего объекта - его id, категории
        item_scan = item.categ + '-' + str(item.pk) + ' , '
        zav.scan  =  str(zav.scan) + str(item_scan)

        # добавление  в объект подходящей заявки (id)
        item.scan = str(item.scan) + ' , ' + str(zav.pk)
        #print("fits_number", type(fits_number), fits_number)
        fits_number=fits_number+1

        print("Соответствие", "item.pk=", item.pk,  "item.categ=", item.categ, "zav.pk=", zav.pk, )


    return fits_number