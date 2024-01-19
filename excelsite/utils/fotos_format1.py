import os
from pathlib import Path
from PIL import Image
import os.path


def format_w (img, width_to):
    width, height = img.size
    aspect = width / height
    width_to=int(width_to)
    height_to = round( width_to / aspect)
    img_formatted = img.resize((width_to, height_to), Image.ANTIALIAS);
    return img_formatted


def go(media_paths, width_to):

    media_osn=media_paths['media_osn']
    media_dop= media_paths['media_dop']


    for  file in os.listdir(media_osn):
        file_path= Path(media_osn, file,  )
        img = Image.open(file_path)
        img_formatted=format_w (img, width_to)
        img_formatted.save(file_path)

    for file in os.listdir(media_dop):
        file_path = Path(media_dop, file, )
        img = Image.open(file_path)
        img_formatted = format_w (img, width_to)
        img_formatted.save(file_path)



        ''' 
        filename = os.path.basename(file)
        basename, extension = os.path.splitext(filename)
        basename = basename + '_form'
        file_formatted = basename + extension
        file_path_to = Path(media_osn, file_formatted)
        print("file_path_to", file_path_to)
        '''


    result = "Фото отформатированы по ширине"
    return result








