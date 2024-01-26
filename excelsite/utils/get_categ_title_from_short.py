def go (item):
    if item.categ == "ofis": result = "Офисы"
    if item.categ == "torg": result = "ТОРГОВАЯ ПЛОЩАДЬ"
    if item.categ == "tc": result = "ЗДАНИЯ"
    if item.categ == "proizv": result = "ПРОИЗВОДСТВО"
    if item.categ == "sklad": result = "СКЛАДЫ"
    if item.categ == "psn": result = "ПСН"
    if item.categ == "retail": result = "РИТЕЙЛ"
    if item.categ == "land": result = "ЗЕМЛЯ"
    if item.categ == "flat": result = "КВАРТИРЫ"
    return result