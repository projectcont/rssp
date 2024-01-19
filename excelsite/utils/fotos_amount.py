import os

def go(media_paths):
    media_osn=media_paths['media_osn']
    media_dop=media_paths['media_dop']
    media_osn_orig=media_paths['media_osn_orig']
    media_dop_orig=media_paths['media_dop_orig']

    n1=str(   len([entry for entry in os.listdir(media_osn) if os.path.isfile(os.path.join(media_osn, entry))])   )
    n2=str(   len([entry for entry in os.listdir(media_dop) if os.path.isfile(os.path.join(media_dop, entry))])   )
    n3=str(  len([entry for entry in os.listdir(media_osn_orig) if os.path.isfile(os.path.join(media_osn_orig, entry))])   )
    n4=str(  len([entry for entry in os.listdir(media_dop_orig) if os.path.isfile(os.path.join(media_dop_orig, entry))])   )

    photos_number= f' media_osn= {n1} </br> ' \
                   f'media_dop= {n2} </br> ' \
                   f'media_osn_orig= {n3} </br> ' \
                   f'media_dop_orig={n4} </br>  '

    return  photos_number