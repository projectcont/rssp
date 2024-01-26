from korp.models import *
from crm.models import *
from utils.scan_fit import fit

def select (price_offset, square_offset):

    # удаление прежних данных по сканам
    Zayavki.objects.all().update(scan="")
    Ofis.objects.all().update(scan="")
    Torg.objects.all().update(scan="")
    Tc.objects.all().update(scan="")
    Proizv.objects.all().update(scan="")
    Sklad.objects.all().update(scan="")
    Psn.objects.all().update(scan="")
    Retail.objects.all().update(scan="")
    Land.objects.all().update(scan="")
    Flat.objects.all().update(scan="")

    # список заявок
    zavs = Zayavki.objects.filter(is_published=True)

    ofis_items = Ofis.objects.filter(is_published=True)
    torg_items = Torg.objects.filter(is_published=True)
    tc_items = Tc.objects.filter(is_published=True)
    proizv_items = Proizv.objects.filter(is_published=True)
    sklad_items = Sklad.objects.filter(is_published=True)
    psn_items = Psn.objects.filter(is_published=True)
    retail_items = Retail.objects.filter(is_published=True)
    land_items = Land.objects.filter(is_published=True)
    flat_items = Flat.objects.filter(is_published=True)


# -----------------------------------------------
    fits_number = 0

    for zav in zavs:

        #print('    next zav')
        for item in torg_items:    fits_number = fit(item, zav, price_offset, square_offset, fits_number  )
        for item in ofis_items:    fits_number = fit(item, zav, price_offset, square_offset, fits_number )

        for item in tc_items:   fits_number =  fit(item, zav, price_offset, square_offset,  fits_number )
        for item in proizv_items:  fits_number =   fit(item, zav, price_offset, square_offset,  fits_number )
        for item in sklad_items:  fits_number =   fit(item, zav, price_offset, square_offset,  fits_number )
        for item in psn_items:  fits_number =   fit(item, zav, price_offset, square_offset,  fits_number )
        for item in retail_items:  fits_number =   fit(item, zav, price_offset, square_offset,  fits_number )
        for item in land_items:  fits_number =   fit(item, zav, price_offset, square_offset,  fits_number )
        for item in flat_items:  fits_number =   fit(item, zav, price_offset, square_offset,  fits_number )

#-----------------------------------------------

    print("bulk_update...")

    Zayavki.objects.bulk_update( zavs, ['scan'])

    Ofis.objects.bulk_update( ofis_items , ['scan'])
    Torg.objects.bulk_update( torg_items, ['scan'])
    Tc.objects.bulk_update( tc_items , ['scan'])
    Proizv.objects.bulk_update( proizv_items , ['scan'])
    Sklad.objects.bulk_update(sklad_items , ['scan'])
    Psn.objects.bulk_update( psn_items, ['scan'])
    Retail.objects.bulk_update( retail_items , ['scan'])
    Land.objects.bulk_update( land_items , ['scan'])
    Flat.objects.bulk_update( flat_items , ['scan'])

    print("bulk_update...finished")

    return fits_number