def go(item)->str:
    n=item.okrug
    if n == '1': result='Центральный';
    if n == '2': result='Северный';
    if n == '3': result='Северо-Восточный';
    if n == '4': result='Восточный';
    if n == '5': result='Юго-Восточный';
    if n == '6': result='Южный';
    if n == '7': result='Юго-Западный';
    if n == '8': result='Западный';
    if n == '9': result='Северо-Западный';
    if n == '10': result='Зеленоградский';
    if n == '11': result='Троицкий';
    if n == '12': result='Новомосковский';
    if n == '13': result = 'неприменимо';
    if n=='100': result='Все округа';
    return result