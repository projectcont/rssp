def check(all_realty):

    for item in all_realty:
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




