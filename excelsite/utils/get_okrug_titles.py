from typing import List

def go(item:List[int])->List[str]:
    '''
    метод из списка округов по id
    возвращает список округов по названиям
    '''


    okrug_list_id=list(item.okrug)
    okrug_list_title=[]
    for n in okrug_list_id:
        if n == '1': okrug_list_title.append('Центральный');
        if n == '2': okrug_list_title.append('Северный');
        if n == '3': okrug_list_title.append('Северо-Восточный');
        if n == '4': okrug_list_title.append('Восточный');
        if n == '5': okrug_list_title.append('Юго-Восточный');
        if n == '6': okrug_list_title.append('Южный');
        if n == '7': okrug_list_title.append('Юго-Западный');
        if n == '8': okrug_list_title.append('Западный');
        if n == '9': okrug_list_title.append('Северо-Западный');
        if n == '10': okrug_list_title.append('Зеленоградский');
        if n == '11': okrug_list_title.append('Троицкий');
        if n == '12': okrug_list_title.append('Новомосковский');
        if n=='1000': okrug_list_title.append('Все округа');
        if n == '1001': okrug_list_title.append('Вне Москвы');


    okrug_str_titles=', '.join(okrug_list_title)

    return okrug_str_titles