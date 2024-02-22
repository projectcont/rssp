def go (all_realty):
    """
    проходит по списку всех объектов и проверяет каждый на возможные ошибки заполнения
    """
    result = " "

    for item in all_realty:

        result_=''
        if item.rent:
            if item.price_rent==None or item.rent_type==None or len(item.rent_type)<2:
                result_= result_+ f"<p> Объект id={item.id} {item.get_categ_title() } <span>в части АРЕНДА не заполнены нужные поля</span> </p> "
                #print(result_)

        if item.sale:
            if item.price_sale == None or item.sale_type==None or item.sale_right==None or len(item.sale_type)<2:
                result_ =  result_+ f"<p> Объект id={item.id}  {item.get_categ_title() } <span>в части ПРОДАЖА не заполнены нужные поля</span> </p>"
                #print(result_)

        if  len(str(item.photo))<2:
            result_ = result_+  f"<p> Объект id={item.id} {item.get_categ_title() } <span>НЕТ ОСНОВНОЙ ФОТО</span> </p>"

        # parking
        if item.categ in ['ofis', 'psn', 'torg', 'tc']:
            if item.parking==None and ( ):
                result_ = result_ + f"<p> Объект id={item.id} {item.get_categ_title()} <span>не указан 'тип парковки'</span> </p>"

        # decoration
        if item.categ in ['ofis', 'psn', 'torg', 'tc', ]:
            if item.otdelka==None :
                result_ = result_ + f"<p> Объект id={item.id} {item.get_categ_title()} <span>не указана 'отделка'</span> </p>"

        # layout
        if item.categ == 'ofis':
            if item.layout==None:
                result_ = result_ + f"<p> Объект id={item.id} {item.get_categ_title()} <span> не указана 'раскладка' для ОФИСА </span> </p>"

        # entrance
        if item.categ in ['psn','torg', ]:
            if item.entrance==None:
                result_ = result_ + f"<p> Объект id={item.id} {item.get_categ_title()} <span> не указан 'вход' </span> </p>"



        result=result+result_


    return  result




