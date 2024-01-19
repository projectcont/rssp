import os
import shutil
from pathlib import Path

def go(media_paths):
    media_osn=media_paths['media_osn']
    media_dop= media_paths['media_dop']
    media_osn_orig= media_paths['media_osn_orig']
    media_dop_orig=media_paths['media_dop_orig']

    for  file in os.listdir(media_osn_orig):

        file_path = Path(media_osn_orig, file, )
        file_path_to= Path(media_osn, file,  )
        shutil.copy2(file_path, file_path_to)

    for  file in os.listdir(media_dop_orig):

        file_path = Path(media_dop_orig, file, )
        file_path_to = Path(media_dop, file, )
        shutil.copy2(file_path, file_path_to)

    result="оригинальные фото восстановлены"

    return result







