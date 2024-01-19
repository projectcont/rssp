def get_rentsale (menu_id=0):
    '''
    для данной кнопки меню
    возвращает строку - аренда ('rent') или продажа ('sale')
    arg  menu_id:int
    return str
    '''

    result='none'

    if menu_id in [11,3,7,9,10,8,4,5 ]:
        result="rent"
    if menu_id in [ 20,21,12,16,18,19,17,13,14]:
        result="sale"

    return result





