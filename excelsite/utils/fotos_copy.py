import os
import shutil
from pathlib import Path

def go(media_paths):
    media_osn=media_paths['media_osn']
    media_dop= media_paths['media_dop']
    media_osn_orig= media_paths['media_osn_orig']
    media_dop_orig=media_paths['media_dop_orig']


    for  file in os.listdir(media_osn):
        file_path= Path(media_osn, file,  )
        file_path_to = Path(media_osn_orig, file, )

        if os.path.exists(file_path_to):
            # проверка, скопирован ли файл ранее
            print(file, '(osn) not-copied')
        else:
            # если не скопирован - копируется
            shutil.copy2(file_path, file_path_to)
            #print(file, '(osn) copied')


    for  file in os.listdir(media_dop):
        file_path= Path(media_dop, file,  )
        file_path_to = Path(media_dop_orig, file, )

        if os.path.exists(file_path_to):
            # проверка, скопирован ли файл ранее
            print(file, '(dop) not-copied')
        else:
            # если не скопирован - копируется
            shutil.copy2(file_path, file_path_to)
            #print(file, '(dop) copied')

    #print()



