from korp.models import  *
def go(item, sale_rent):
    xml_list=[]

    #id
    el = f'<Id>{item.idl}</Id>'
    xml_list.append(el)

    #Description
    description=item.description
    description=description.replace('&laquo;','«')
    description=description.replace('&raquo;', '»')
    description = description.replace('&774;', '')


    el =  f'<Description>{description}</Description>'
    xml_list.append(el)

    #Address
    el =  f'<Address>{item.adres}</Address>'
    xml_list.append(el)


    #Category
    if item.categ == 'land':
        el =   f'<Category>Земельные участки</Category>'
        xml_list.append(el)
    elif item.categ == 'flat':
        el =   f'<Category>Квартиры</Category>'
        xml_list.append(el)
    else:
        el =   f'<Category>Коммерческая недвижимость</Category>'
        xml_list.append(el)



    # Price
    if sale_rent == "rent":
        el =  f'<Price>{item.price_rent}</Price>'
        xml_list.append(el)
    if sale_rent == "sale":
        el =  f'<Price>{item.price_sale}</Price>'
        xml_list.append(el)

    #OperationType
    if sale_rent=='sale':
        el =  f'<OperationType>Продам</OperationType>'
        xml_list.append(el)
    if sale_rent == 'rent':
        el =  f'<OperationType>Сдам</OperationType>'
        xml_list.append(el)


    # ObjectType
    if item.categ == 'ofis': ObjectType='Офисное помещение'
    if item.categ == 'torg': ObjectType = 'Торговое помещение'
    if item.categ == 'tc': ObjectType = 'Здание'
    if item.categ == 'proizv': ObjectType = 'Производственное помещение'
    if item.categ == 'sklad': ObjectType = 'Складское помещение'
    if item.categ == 'psn': ObjectType =  'Помещение свободного назначения'
    if item.categ == 'land': ObjectType = item.land_type
    el =  f'<ObjectType>{ObjectType}</ObjectType>'
    xml_list.append(el)


    # Entrance
    if item.categ in ['torg', 'psn', ]:
        el =  f'<Entrance>{item.entrance}</Entrance>'
        xml_list.append(el)

    # Floor
    if item.categ not in ['tc', 'land',]:
        el =  f'<Floor>{item.floor}</Floor>'
        xml_list.append(el)

    # Layout
    if item.categ in ['ofis', ]:
        el =  f'<Layout>{item.layout}</Layout>'
        xml_list.append(el)

    # square
    if item.categ not in ['land',  ]:
        el =  f'<Square>{item.square}</Square>'
        xml_list.append(el)

    #Decoration
    if item.categ in ['ofis', 'psn', 'torg', 'tc', ]:
        el =  f'<Decoration>{item.otdelka}</Decoration>'
        xml_list.append(el)

    # BuildingType
    if item.categ not in ['land', 'flat', ]:
        el =  f'<BuildingType>{item.buildtype}</BuildingType>'
        xml_list.append(el)

    # ParkingType
    if item.categ in ['ofis', 'psn', 'torg', 'tc']:
        el =  f'<ParkingType>{item.parking}</ParkingType>'
        xml_list.append(el)

    #RentalType
    if sale_rent=="rent":
        el =  f'<RentalType>{item.rent_type}</RentalType>'
        xml_list.append(el)

    # TransactionType
    if sale_rent == "sale":
        el =  f'<TransactionType>{item.sale_type}</TransactionType>'
        xml_list.append(el)

    el = f'<PropertyRights>{item.sale_right}</PropertyRights>'
    xml_list.append(el)


    #LandArea
    if item.categ == 'land':
        el =  f'<LandArea>{item.landarea}</LandArea>'
        xml_list.append(el)

    #----------images-------------------

    BASE_URL="https://gebo-commers.ru/mediafiles/"

    photo_url=BASE_URL+str(item.photo)

    images_urls=[photo_url]

    for n in ['photo1', 'photo2','photo3','photo4','photo5','photo6','photo7','photo8','photo9','photo10',  ]:
        url=str(getattr(item, n))
        if (url is None) or (len(url)<2) :
            pass
        else:
            full_url=BASE_URL+url
            images_urls.append(full_url)
    print('images_urls=', images_urls)

    image_tags=''
    for n in images_urls:
        image_tag= f'<Image url = "{n}" />'
        image_tags =image_tags + image_tag

    el = f'<Images>{image_tags}</Images>'
    xml_list.append(el)

    # ----------images-------------------


    # склейка всех xml-тегов данного объекта
    xml_item= "\n".join(xml_list)

    xml_item_=f'\n<Ad>\n{xml_item}\n</Ad>\n'
    #print('xml_item=', xml_item_)


    return  xml_item_

