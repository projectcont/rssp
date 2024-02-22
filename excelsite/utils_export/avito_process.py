import  utils.scan_lenths
from  utils_export.avito_item import go as get_xml_item
from  crm.models import Export
def go(all_realty):


    for item in all_realty:

        #if item.sale_type and item.sale_type == '1': item.sale_type='Продажа'
        #if item.sale_type and item.sale_type == '2': item.sale_type = 'Переуступка прав аренды'
        #if item.rent_type and item.rent_type == '1': item.rent_type='Прямая'
        #if item.rent_type and item.rent_type == '2': item.rent_type = 'Субаренда'
        item.idl=item.categ+'-'+str(item.id)+'-'+'gebocommers'
        item.save()
        #print("item.save",item.idl)

    print("idl setted")

    avito = Export.objects.get(pk=1)
    using = avito.using
    xmlfile_path="../filesexp/avito.xml"


    xml_items=''
    counter=0

    # ----------------------если на авито указано  не отправлять
    if int(using)==0:
        xml_items=''

    # ------------------------если на авито указано отправлять все объекты
    if int(using)==2:
        # для продажи
        sale_rent='sale'
        for item in all_realty:
            print("item pk sale",item.pk)
            if item.sale:
                xml_item=get_xml_item(item,sale_rent)
                xml_items=xml_items+xml_item
                counter = counter+1
        # для аренды
        sale_rent = 'rent'
        for item in all_realty:
            print("item pk rent", item.pk)
            if item.rent:
                xml_item =  get_xml_item(item, sale_rent)
                xml_items = xml_items + xml_item
                counter = counter + 1

    # -------------------------------если на авито указано отправлять объекты по выбору
    if int(using) == 1:
        # для продажи
        sale_rent = 'sale'
        for item in all_realty:
            if ((item.sale) and (item.export_avito)):
                xml_item = get_xml_item(item, sale_rent)
                xml_items = xml_items + xml_item
                counter = counter + 1

        # для аренды
        sale_rent = 'rent'
        for item in all_realty:
            if ((item.rent) and (item.export_avito)):
                xml_item = get_xml_item(item, sale_rent)
                xml_items = xml_items + xml_item
                counter = counter + 1


    xml_wrapper = f'<?xml version="1.0" encoding="UTF-8"?><Ads formatVersion="3" target="Avito.ru">{xml_items}</Ads>'

    # Writing to file
    with open(xmlfile_path, "w", encoding="utf-8") as file:
        # Writing data to a file
        file.write(xml_wrapper)

    return counter