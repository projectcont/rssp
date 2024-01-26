def color_ (scan, zavs_bd_len, realty_bd_len):
    """
    функция определяет, нужно ли сканирование
    args scan - список сканов
    zavs_bd_len -  длина списка заявок
    realty_bd_len - длина списка объектов
    """
    realty_number = scan.realty_number
    zav_number = scan.zav_number
    check_zavs = check_realty = check = 1
    if (zav_number != zavs_bd_len ): check_zavs = 0
    if (realty_number != realty_bd_len ): check_realty = 0
    if (check_zavs == 0) or (check_realty) == 0:  check = 0
    return check_zavs, check_realty, check, zav_number, realty_number